#!/bin/bash
#
# The script use a PDF file (usually from NotebookLM or PowerPoint) and converts each page
# into a PNG file (use `magick` with `-density 200`). The PNG files are stored in `${IMAGES_DIR}`
# The filename for each image is derived from the original filename (replace any special char)
# with '-'. The filename is of the format <MODIFIED-ORIG-FILENAME>-NN.png with NN the slide number, user leading 0s
# The script also produces a Markdown entry for each slide
# ```
# ***
#
# {{< slide content-image="/imgs/Engineering_Agentic_Governance_00.png" >}}
# <h1></h1>
#
# ```
#
# Usage:
#     copnvert_pdf_to_hugo.sh PDF_FILE [SLIDE_FILE]
# If SLIDE_FILE not defined use STDOUT
# If defined and SLIDE_FILE is just a file and does not contain '/' or directory path,
#  then write  Markdown to the file in ${SLIDES_DIR}. The file has to have the extesion '.md'
#  if missing ad '.md'. If the file exists, append ... do not overwrite.
# If file is a path, even `./output.md` attempt to append te to this file.

set -euo pipefail

ROOT_DIR="$(realpath "$(dirname "$0")/..")"
SLIDES_DIR="${ROOT_DIR}/content/slides"
# Images must live under static/ so Hugo serves them at the /imgs/... URL used below.
IMAGES_DIR="${ROOT_DIR}/static/imgs"
IMAGES_URL="/imgs"

DENSITY=200
# Separator between the sanitized base name and the page number.
# Matches the existing images in static/imgs (e.g. Engineering_Multimodal_Intelligence_00.png).
SEP="_"

usage() {
    echo "Usage: $(basename "$0") PDF_FILE [SLIDE_FILE]" >&2
    echo "  PDF_FILE    PDF to split into one PNG per page (written to ${IMAGES_DIR})" >&2
    echo "  SLIDE_FILE  Markdown output. Bare name -> appended to ${SLIDES_DIR} ('.md' added" >&2
    echo "              if missing); any name containing '/' is used as given. Omit for STDOUT." >&2
}

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    usage
    exit 1
fi

PDF_FILE="$1"
SLIDE_FILE="${2:-}"

if [ ! -f "${PDF_FILE}" ]; then
    echo "Error: PDF file not found: ${PDF_FILE}" >&2
    exit 1
fi

if ! command -v magick >/dev/null 2>&1; then
    echo "Error: 'magick' (ImageMagick 7) not found in PATH." >&2
    echo "       Install with: brew install imagemagick ghostscript" >&2
    exit 1
fi

# --- derive the image base name from the PDF filename -------------------------
# Strip the directory and the .pdf extension, then replace every run of
# non-alphanumeric characters with the separator and trim it from both ends.
BASE_NAME="$(basename "${PDF_FILE}")"
BASE_NAME="${BASE_NAME%.[Pp][Dd][Ff]}"
BASE_NAME="$(printf '%s' "${BASE_NAME}" \
    | sed -E "s/[^[:alnum:]]+/${SEP}/g; s/^${SEP}+//; s/${SEP}+$//")"

if [ -z "${BASE_NAME}" ]; then
    echo "Error: could not derive a usable name from '${PDF_FILE}'." >&2
    exit 1
fi

# --- resolve the Markdown output target ---------------------------------------
# Empty OUT_FILE means STDOUT.
OUT_FILE=""
if [ -n "${SLIDE_FILE}" ]; then
    case "${SLIDE_FILE}" in
        */*)
            # A path (even './output.md') is used verbatim.
            OUT_FILE="${SLIDE_FILE}"
            ;;
        *)
            # A bare name goes into the slides directory and must end in .md
            case "${SLIDE_FILE}" in
                *.md) ;;
                *) SLIDE_FILE="${SLIDE_FILE}.md" ;;
            esac
            OUT_FILE="${SLIDES_DIR}/${SLIDE_FILE}"
            ;;
    esac

    OUT_DIR="$(dirname "${OUT_FILE}")"
    if [ ! -d "${OUT_DIR}" ]; then
        echo "Error: output directory does not exist: ${OUT_DIR}" >&2
        exit 1
    fi
fi

# --- render the PDF pages ------------------------------------------------------
mkdir -p "${IMAGES_DIR}"

# Render into a temporary directory first so the page count is exact and stale
# images from an earlier (longer) run cannot be mistaken for pages of this PDF.
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

echo "Rendering '${PDF_FILE}' at ${DENSITY} dpi ..." >&2
magick -density "${DENSITY}" "${PDF_FILE}" -background white -alpha remove -alpha off \
    "${TMP_DIR}/page-%04d.png"

# Sorted list of rendered pages (page-0000.png, page-0001.png, ...).
PAGES=()
while IFS= read -r page; do
    PAGES+=("${page}")
done < <(find "${TMP_DIR}" -maxdepth 1 -name 'page-*.png' | sort)

PAGE_COUNT="${#PAGES[@]}"
if [ "${PAGE_COUNT}" -eq 0 ]; then
    echo "Error: no pages were rendered from '${PDF_FILE}'." >&2
    exit 1
fi

# At least two digits, more if the deck has 100+ slides.
WIDTH=${#PAGE_COUNT}
[ "${WIDTH}" -lt 2 ] && WIDTH=2

# --- move the images into place and build the Markdown -------------------------
MARKDOWN=""
INDEX=0
for page in "${PAGES[@]}"; do
    IMAGE_NAME="$(printf '%s%s%0*d.png' "${BASE_NAME}" "${SEP}" "${WIDTH}" "${INDEX}")"
    mv -f "${page}" "${IMAGES_DIR}/${IMAGE_NAME}"
    echo "  ${IMAGES_DIR}/${IMAGE_NAME}" >&2

    MARKDOWN+="***"$'\n\n'
    MARKDOWN+="{{< slide content-image=\"${IMAGES_URL}/${IMAGE_NAME}\" >}}"$'\n'
    MARKDOWN+="<h1></h1>"$'\n\n'

    INDEX=$((INDEX + 1))
done

echo "Converted ${PAGE_COUNT} page(s)." >&2

# --- emit the Markdown ---------------------------------------------------------
if [ -z "${OUT_FILE}" ]; then
    printf '%s' "${MARKDOWN}"
else
    # Append, never overwrite.
    printf '%s' "${MARKDOWN}" >> "${OUT_FILE}"
    echo "Markdown appended to ${OUT_FILE}" >&2
fi
