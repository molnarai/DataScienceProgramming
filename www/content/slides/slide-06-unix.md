+++
title = "Unix File System and Command Line"
description = "The file tree, the shell, text streams, redirection and pipes — the small composable tools behind every data workflow"
weight = 60
outputs = ["Reveal"]
math = false
thumbnail = "/imgs/slides/Building_Blocks_of_Modern_Computing.png"

[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-sub { color: #666; font-size: 0.9em; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-small { font-size: 0.75em; }
  .reveal .dc-muted { color: #666; }

  /* Cards */
  .reveal .dc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 14px; }
  .reveal .dc-grid.three { grid-template-columns: 1fr 1fr 1fr; }
  .reveal .dc-card { background: #f4f6f9; border-left: 5px solid #003478; padding: 10px 14px; border-radius: 4px; }
  .reveal .dc-card h3 { margin: 0 0 4px 0; font-size: 0.85em; }
  .reveal .dc-card p { margin: 0; font-size: 0.62em; }
  .reveal .dc-card .dc-from { color: #666; font-size: 0.58em; margin-bottom: 6px; }
  .reveal .dc-card.red { border-left-color: #CC0000; }
  .reveal .dc-card.red h3 { color: #CC0000; }
  .reveal .dc-card.green { border-left-color: #2e7d32; }
  .reveal .dc-card.green h3 { color: #2e7d32; }

  /* Flow */
  .reveal .dc-flow { display: flex; align-items: center; justify-content: center; gap: 8px; margin: 20px 0; }
  .reveal .dc-node { background: #f4f6f9; border: 2px solid #003478; border-radius: 6px; padding: 10px 14px; font-size: 0.62em; text-align: center; font-family: var(--r-code-font); }
  .reveal .dc-node.dark { background: #003478; color: #fff; }
  .reveal .dc-node .dc-owner { margin-top: 4px; font-size: 0.85em; font-style: italic; color: #CC0000; font-family: var(--r-main-font); }
  .reveal .dc-node.dark .dc-owner { color: #cfd8e8; }
  .reveal .dc-arrow { color: #003478; font-size: 0.9em; font-weight: 700; }

  /* Two columns */
  .reveal .dc-cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start; }
  .reveal .dc-cols h4 { font-size: 0.65em; margin: 6px 0 0 0; }
  .reveal .dc-cols h4.bad { color: #CC0000; }
  .reveal .dc-cols h4.good { color: #2e7d32; }

  /* Code */
  .reveal .highlight pre, .reveal pre { width: 100%; font-size: 0.5em; margin: 8px 0; }
  .reveal .dc-code-lg pre { font-size: 0.58em; }

  /* Terminal */
  .reveal .dc-term { background: #12233b; color: #e8edf4; border-radius: 6px; padding: 12px 16px; font-family: var(--r-code-font); font-size: 0.52em; text-align: left; line-height: 1.45; margin: 10px 0; }
  .reveal .dc-term .p { color: #7fb3ff; }
  .reveal .dc-term .c { color: #ffffff; font-weight: 700; }
  .reveal .dc-term .o { color: #9fb3c8; }
  .reveal .dc-term .g { color: #6fd08c; }
  .reveal .dc-term .e { color: #ff8a70; }
  .reveal .dc-term .cm { color: #8a9bb0; font-style: italic; }

  /* Bullets */
  .reveal .dc-points { margin-top: 8px; }
  .reveal .dc-points li { font-size: 0.72em; margin-bottom: 0.4em; }

  /* Tag row */
  .reveal .dc-map { display: flex; gap: 10px; align-items: center; font-size: 0.6em; margin: 0 0 10px 0; }
  .reveal .dc-map span { padding: 3px 10px; border-radius: 12px; background: #f4f6f9; border: 1px solid #003478; }
  .reveal .dc-map span.py { background: #003478; color: #fff; }

  .reveal .dc-table { font-size: 0.58em; width: 100%; margin-top: 10px; }
  .reveal .dc-table td { vertical-align: top; }
  .reveal .dc-table td:first-child { width: 36%; }
  .reveal .dc-table code { font-size: 0.95em; }

  .reveal .dc-nb { font-size: 0.6em; }
  .reveal .dc-nb .num { display: inline-block; width: 1.6em; height: 1.6em; line-height: 1.6em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-weight: 700; margin-right: 6px; }
  .reveal .dc-path { font-family: var(--r-code-font); font-size: 0.6em; background: #f4f6f9; border: 1px solid #ccc; border-radius: 4px; padding: 8px 12px; display: inline-block; }
  .reveal .dc-warn { background: #fff4f2; border-left: 5px solid #CC0000; padding: 10px 14px; border-radius: 4px; font-size: 0.62em; text-align: left; margin-top: 14px; }
</style>

<p class="dc-kicker">IFI 8410 — Session 6: Unix File System and Command Line</p>
<h1>The Blueprint of Modern Computing</h1>
<p class="dc-sub">One tree, small tools, and text flowing between them</p>

{{% note %}}
Session 5 ended with scripts that read and write files. This session is about the environment those scripts run in: where the files are, how you get to them, and how programs are connected to one another.
{{% /note %}}

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-00.png" >}}
<h1></h1>

***

<p class="dc-kicker">Where we are going</p>

## Today in four moves

<div class="dc-grid">
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">1</span></span>Where it came from</h3><p class="dc-from">Ideas, not just an OS</p><p>Multics → UNIX → BSD, Linux, macOS. Why a 1970s design still runs the cloud.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>The tree and the shell</h3><p class="dc-from">Knowing where you are</p><p>One root, paths, the working directory, and the commands that move and organize.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">3</span></span>Streams and pipes</h3><p class="dc-from">Composition</p><p><code>stdin</code>, <code>stdout</code>, <code>stderr</code>; redirection with <code>&gt;</code>; pipelines with <code>|</code>.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">4</span></span>Your own tools</h3><p class="dc-from">From typing to scripting</p><p>Permissions, executable scripts, and running Python from the shell.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;">Running example: <b>what are the most frequent words in Shakespeare?</b> — answered without writing a program.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-01.png" >}}
<h1></h1>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-02.png" >}}
<h1></h1>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-03.png" >}}
<h1></h1>

***

<p class="dc-kicker">Which one am I on?</p>

## The family is real, and you are in it

<div class="dc-term">
<span class="p">$</span> <span class="c">uname -s</span><br>
<span class="o">Darwin</span>          <span class="cm"># macOS — a certified UNIX, BSD lineage</span><br>
<span class="o">Linux</span>           <span class="cm"># the ARC cluster, most servers, WSL</span><br>
<br>
<span class="p">$</span> <span class="c">echo $SHELL</span><br>
<span class="o">/bin/zsh</span>        <span class="cm"># default on macOS</span><br>
<span class="o">/bin/bash</span>       <span class="cm"># default on most Linux systems</span>
</div>

<ul class="dc-points">
  <li>The commands in this session work the same in <code>bash</code> and <code>zsh</code>.</li>
  <li>Small differences exist between <b>GNU</b> (Linux) and <b>BSD</b> (macOS) versions of tools — check <code>man command</code> on your own machine.</li>
  <li><b>Windows:</b> use WSL, or work on the course server over SSH.</li>
</ul>

{{% note %}}
Ask the room to run uname -s and echo $SHELL right now. It takes ten seconds and establishes that everyone has a Unix to work in before anything else is attempted.
{{% /note %}}

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-04.png" >}}
<h1></h1>

***

<p class="dc-kicker">Do one thing well</p>

## Each tool is almost insultingly simple

<div class="dc-cols">
  <div>
{{< highlight bash >}}
wc -l   # count lines
sort    # put lines in order
uniq -c # collapse repeats, with a count
grep    # keep lines that match
head    # show the first few
tr      # translate or delete characters
{{< /highlight >}}
  </div>
  <div>
    <ul class="dc-points" style="margin-top: 0;">
      <li>None of them knows anything about your data.</li>
      <li>None of them opens a window, asks a question, or holds state.</li>
      <li>Each reads <b>text in</b> and writes <b>text out</b> — which is exactly why they can be combined.</li>
    </ul>
  </div>
</div>

<p class="dc-small" style="margin-top: 14px;">The power is not in any one tool. It is in the <b>interface they share</b>.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-05.png" >}}
<h1></h1>

***

<p class="dc-kicker">Reading a command line</p>

## Command, options, arguments

<div class="dc-flow" style="margin-top: 30px;">
  <div class="dc-node dark">ls<div class="dc-owner">the program</div></div>
  <div class="dc-node">-la<div class="dc-owner">options / flags</div></div>
  <div class="dc-node">projects<div class="dc-owner">argument</div></div>
</div>

<div class="dc-term">
<span class="p">$</span> <span class="c">ls -la projects</span><br>
<span class="o">total 24</span><br>
<span class="o">drwxr-xr-x   5 student  staff   160 Sep 30 09:12 .</span><br>
<span class="o">drwxr-xr-x  12 student  staff   384 Sep 30 09:10 ..</span><br>
<span class="o">-rw-r--r--   1 student  staff  1044 Sep 30 09:12 notes.txt</span>
</div>

<p class="dc-small">The <b>shell</b> reads the line, expands shorthand such as <code>~</code> and <code>*</code>, then starts the program. The program never sees the wildcard — only the filenames it matched.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-06.png" >}}
<h1></h1>

***

<p class="dc-kicker">Why bother</p>

## When the shell is the right tool

<div class="dc-grid">
  <div class="dc-card green"><h3>Remote work</h3><p>Over SSH there is often no desktop at all — the cluster, the server, the container.</p></div>
  <div class="dc-card green"><h3>Repetition</h3><p>The same operation on 10,000 files, run again next month with one command.</p></div>
  <div class="dc-card green"><h3>Composition</h3><p>Ad-hoc questions answered by connecting tools no one wrote for that question.</p></div>
  <div class="dc-card green"><h3>Reproducibility</h3><p>A recorded command is evidence; a sequence of mouse clicks is a memory.</p></div>
</div>

<p class="dc-small" style="margin-top: 16px;">The terminal is not an alternative to programming — it is one of the environments programming happens in.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-07.png" >}}
<h1></h1>

***

<p class="dc-kicker">Knowing where you are</p>

## Three commands, most of the time

<div class="dc-term">
<span class="p">$</span> <span class="c">pwd</span>                        <span class="cm"># print working directory</span><br>
<span class="o">/home/student/ifi8410</span><br>
<br>
<span class="p">$</span> <span class="c">ls data</span>                    <span class="cm"># what is in there?</span><br>
<span class="o">scores.csv  shakespeare.txt</span><br>
<br>
<span class="p">$</span> <span class="c">cd data</span>                    <span class="cm"># go somewhere else</span><br>
<span class="p">$</span> <span class="c">cd ..</span>                      <span class="cm"># back up one level</span><br>
<span class="p">$</span> <span class="c">cd ~</span>                       <span class="cm"># home</span><br>
<span class="p">$</span> <span class="c">cd -</span>                       <span class="cm"># back where I just was</span>
</div>

<div class="dc-cols" style="margin-top: 10px;">
  <div><p class="dc-small"><b>Absolute</b> — from the root, means the same anywhere:<br><span class="dc-path">/home/student/ifi8410/data/scores.csv</span></p></div>
  <div><p class="dc-small"><b>Relative</b> — from where you stand right now:<br><span class="dc-path">data/scores.csv</span></p></div>
</div>

{{% note %}}
The single most common beginner error is a path that is correct for a different working directory. "No such file or directory" almost always means pwd is not where you assumed.
{{% /note %}}

***

<p class="dc-kicker">Building a workspace</p>

## Create, copy, move, remove

<div class="dc-term">
<span class="p">$</span> <span class="c">mkdir -p project/data project/out</span>   <span class="cm"># -p: make parents, don't complain</span><br>
<span class="p">$</span> <span class="c">cp notes.txt project/</span>               <span class="cm"># copy (-r for directories)</span><br>
<span class="p">$</span> <span class="c">mv notes.txt project/README.txt</span>     <span class="cm"># move — and rename</span><br>
<span class="p">$</span> <span class="c">rm project/out/draft.txt</span>            <span class="cm"># remove. permanently.</span>
</div>

<ul class="dc-points">
  <li>Separate <b>inputs</b> from <b>outputs</b>: you can delete <code>out/</code> and rebuild it without risking data.</li>
  <li><code>cp</code> and <code>mv</code> overwrite the target <b>without asking</b>.</li>
</ul>

<div class="dc-warn">
  <b>rm has no undo and no trash can.</b> Before <code>rm -r</code> with a wildcard, run <code>ls</code> on the same pattern and read what it matched. Check <code>pwd</code> first.
</div>

***

<p class="dc-kicker">Looking without opening</p>

## A 5 MB file is not for your editor

<div class="dc-term">
<span class="p">$</span> <span class="c">wc -l data/shakespeare.txt</span><br>
<span class="o">  196024 data/shakespeare.txt</span><br>
<br>
<span class="p">$</span> <span class="c">head -n 3 data/pg100.txt</span>            <span class="cm"># first lines; tail for the last</span><br>
<span class="o">The Project Gutenberg eBook of The Complete Works of William Shakespeare</span><br>
<span class="o">&nbsp;</span><br>
<span class="o">This eBook is for the use of anyone anywhere in the United States and</span><br>
<span class="cm">                                        # ...so the file is not all Shakespeare</span><br>
<br>
<span class="p">$</span> <span class="c">grep -c -i -w "love" data/shakespeare.txt</span>  <span class="cm"># lines containing the word</span><br>
<span class="o">2342</span>
</div>

<p class="dc-small"><code>less file</code> pages through interactively — <code>space</code> scrolls, <code>/</code> searches, <code>q</code> quits. It never loads the whole file into memory, so it opens a gigabyte instantly.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-08.png" >}}
<h1></h1>

***

<p class="dc-kicker">Reading the nine characters</p>

## Permissions in practice

<div class="dc-term">
<span class="p">$</span> <span class="c">ls -l wordfreq.sh</span><br>
<span class="o">-rw-r--r--  1 student  staff  219 Sep 30 11:02 wordfreq.sh</span><br>
<span class="cm">   ^^^ ^^^ ^^^   owner / group / others — r read, w write, x execute</span><br>
<br>
<span class="p">$</span> <span class="c">chmod +x wordfreq.sh</span>            <span class="cm"># add execute permission</span><br>
<span class="p">$</span> <span class="c">ls -l wordfreq.sh</span><br>
<span class="g">-rwxr-xr-x</span><span class="o">  1 student  staff  219 Sep 30 11:02 wordfreq.sh</span><br>
<br>
<span class="p">$</span> <span class="c">./wordfreq.sh</span>                   <span class="cm"># ./ = "the file here", not on $PATH</span>
</div>

<ul class="dc-points">
  <li>On a <b>directory</b>, <code>x</code> means "may enter" — without it you cannot <code>cd</code> in, even if you can read it.</li>
  <li><code>chmod 755</code> is the same as <code>rwxr-xr-x</code> — one digit per class.</li>
</ul>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-09.png" >}}
<h1></h1>

***

<p class="dc-kicker">Why two output channels</p>

## Results and complaints travel separately

<div class="dc-cols">
  <div class="dc-code-lg">
{{< highlight python >}}
import sys

# the answer — the next program's input
print(f"{count} {word}")

# the commentary — for a human
print("warning: 3 rows skipped",
      file=sys.stderr)
{{< /highlight >}}
  </div>
  <div>
    <ul class="dc-points" style="margin-top: 0;">
      <li>If warnings went to <code>stdout</code>, they would land in your data file.</li>
      <li>Mixing them is the single most common way to corrupt a pipeline.</li>
      <li>Rule of thumb: <b>anything a human reads</b> goes to <code>stderr</code>; anything a <b>program</b> reads goes to <code>stdout</code>.</li>
    </ul>
  </div>
</div>

<p class="dc-small" style="margin-top: 12px;">Same rule in the shell: <code>echo</code> results, but send progress messages with <code>echo "..." &gt;&amp;2</code>.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-10.png" >}}
<h1></h1>

***

<p class="dc-kicker">Repointing the channels</p>

## Redirection, four symbols

<div class="dc-term">
<span class="p">$</span> <span class="c">python3 summarize.py data.csv &gt; summary.txt</span>   <span class="cm"># stdout to a file (replaces)</span><br>
<span class="p">$</span> <span class="c">echo "run 2" &gt;&gt; log.txt</span>                       <span class="cm"># append instead of replace</span><br>
<span class="p">$</span> <span class="c">sort &lt; names.txt</span>                             <span class="cm"># stdin from a file</span><br>
<span class="p">$</span> <span class="c">python3 summarize.py data.csv 2&gt; problems.txt</span> <span class="cm"># stderr to its own file</span><br>
<br>
<span class="p">$</span> <span class="c">ls data/real.txt data/missing.txt &gt; found.txt 2&gt; errors.txt</span><br>
<span class="p">$</span> <span class="c">cat errors.txt</span><br>
<span class="e">ls: data/missing.txt: No such file or directory</span>
</div>

<div class="dc-cols" style="margin-top: 8px;">
  <div><p class="dc-small"><code>2&gt;&amp;1</code> merges stderr into stdout — one combined stream.</p></div>
  <div><p class="dc-small"><code>2&gt;/dev/null</code> discards errors entirely. Use it deliberately, not by habit.</p></div>
</div>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-11.png" >}}
<h1></h1>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-12.png" >}}
<h1></h1>

***

<p class="dc-kicker">Building it one stage at a time</p>

## Most frequent words in Shakespeare

<div class="dc-code-lg">
{{< highlight bash >}}
tr -d '.,:;?!"()[]' < data/shakespeare.txt \
| tr 'A-Z' 'a-z' \
| tr -s ' \t\r' '\n' \
| grep -v -e '^[[:space:]]*$' \
| sort \
| uniq -c \
| sort -rn \
| head -n 5
{{< /highlight >}}
</div>

<div class="dc-cols">
  <div>
    <div class="dc-term" style="font-size: 0.5em;">
      <span class="o">30249 the</span><br>
      <span class="o">28388 and</span><br>
      <span class="o">21672 i</span><br>
      <span class="o">20598 to</span><br>
      <span class="o">18736 of</span>
    </div>
  </div>
  <div>
    <ul class="dc-points" style="margin-top: 0; font-size: 0.95em;">
      <li>Six tools, no program, no temporary files.</li>
      <li>Each stage is <b>inspectable on its own</b> — pipe into <code>head</code> and look.</li>
      <li>The answer is function words — which is itself the finding.</li>
    </ul>
  </div>
</div>

{{% note %}}
Build this live, one stage at a time, ending each with | head. Students should see that the pipeline is developed by inspection, not written correctly in one go.
{{% /note %}}

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-13.png" >}}
<h1></h1>

***

<p class="dc-kicker">From typing to tooling</p>

## A pipeline you repeat is a script

<div class="dc-cols">
  <div class="dc-code-lg">
{{< highlight bash >}}
#!/bin/bash
# Read text on stdin,
# write "count word" on stdout.
tr -d '.,:;?!"()[]' \
| tr 'A-Z' 'a-z' \
| tr -s ' \t\r' '\n' \
| grep -v -e '^[[:space:]]*$' \
| sort | uniq -c | sort -rn
{{< /highlight >}}
  </div>
  <div>
    <ul class="dc-points" style="margin-top: 0;">
      <li><b>Hash-bang</b> <code>#!/bin/bash</code> on line 1 names the interpreter.</li>
      <li><code>chmod +x wordfreq.sh</code> makes it runnable.</li>
      <li>No filenames inside — it reads <code>stdin</code>, so it <b>composes like a built-in tool</b>.</li>
    </ul>
  </div>
</div>

<div class="dc-term" style="margin-top: 6px;">
<span class="p">$</span> <span class="c">sed -n '/HAMLET/,/KING HENRY/p' data/shakespeare.txt | ./wordfreq.sh | head -3</span><br>
<span class="o">1112 the</span><br>
<span class="o"> 980 and</span><br>
<span class="o"> 725 to</span>
</div>

***

<p class="dc-kicker">The shell starts your programs too</p>

## Running Python from the command line

<div class="dc-cols">
  <div class="dc-code-lg">
{{< highlight python >}}
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("usage: wordfreq.py FILE [N]",
              file=sys.stderr)
        return 1                  # exit status
    path = Path(sys.argv[1])
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    ...

if __name__ == "__main__":
    sys.exit(main())
{{< /highlight >}}
  </div>
  <div>
    <div class="dc-term" style="font-size: 0.48em;">
      <span class="p">$</span> <span class="c">python3 wordfreq.py shakespeare.txt 5</span><br>
      <span class="o">   30249 the</span><br>
      <span class="o">   28388 and</span><br>
      <br>
      <span class="p">$</span> <span class="c">python3 wordfreq.py</span><br>
      <span class="e">usage: wordfreq.py FILE [N]</span><br>
      <span class="p">$</span> <span class="c">echo $?</span><br>
      <span class="o">1</span>      <span class="cm"># 0 = success</span>
    </div>
    <ul class="dc-points" style="font-size: 0.68em;">
      <li><code>sys.argv</code> carries the words after the command.</li>
      <li>The <b>exit status</b> is how scripts test whether a step worked.</li>
    </ul>
  </div>
</div>

***

<p class="dc-kicker">Same operating system, two dialects</p>

## The shell command and its Python twin

<table class="dc-table">
  <thead><tr><th>Shell</th><th>Python</th></tr></thead>
  <tbody>
    <tr><td><code>pwd</code></td><td><code>Path.cwd()</code></td></tr>
    <tr><td><code>ls</code></td><td><code>Path(".").iterdir()</code> · <code>Path(".").glob("*.csv")</code></td></tr>
    <tr><td><code>mkdir -p out/reports</code></td><td><code>Path("out/reports").mkdir(parents=True, exist_ok=True)</code></td></tr>
    <tr><td><code>cp</code> · <code>mv</code> · <code>rm</code></td><td><code>shutil.copy()</code> · <code>shutil.move()</code> · <code>Path.unlink()</code></td></tr>
    <tr><td><code>~</code></td><td><code>Path.home()</code></td></tr>
    <tr><td><code>cmd &gt; file</code> · <code>cmd 2&gt; file</code></td><td><code>sys.stdout</code> · <code>sys.stderr</code></td></tr>
  </tbody>
</table>

<p class="dc-small" style="margin-top: 12px;">Neither is "the real way". The shell is for <b>interactive work and quick composition</b>; Python is for <b>logic that belongs in a program</b>.</p>

***

{{< slide content-image="/imgs/the-unix-blueprint/the-unix-blueprint-14.png" >}}
<h1></h1>

***

<p class="dc-kicker">Now: hands-on</p>

## Open a terminal

<div class="dc-grid">
  <div class="dc-card green"><h3><span class="dc-nb"><span class="num">1</span></span>Notebook</h3><p class="dc-from">Guided</p><p><a href="https://github.com/molnarai/DataScienceProgramming/tree/main/06-Unix-Command-Line"><code>06-Unix-Command-Line</code></a> — the word-frequency pipeline, built stage by stage, with a <i>Your turn</i> section at the end.</p></div>
  <div class="dc-card"><h3><span class="dc-nb"><span class="num">2</span></span>Read</h3><p class="dc-from">Reference</p><p><a href="../../blog/unix-file-system-command-line/">File System and CLI</a> for the commands, <a href="../../blog/unix-core-idea/">UNIX Overview</a> for the ideas, <a href="../../blog/unix-reference/">UNIX Reference</a> to go further.</p></div>
</div>

<p class="dc-small" style="margin-top: 18px;"><b>Homework 5</b> — organize a directory tree from the shell, run your scripts from the command line, and show the commands you used. Due Wednesday, October 14.</p>

{{% note %}}
Have everyone open a real terminal, not only the notebook. The notebook's %%sh cells are convenient but each one is a fresh shell — cd does not persist between cells, which confuses students who never leave the notebook.
{{% /note %}}

***

<p class="dc-kicker">Take away</p>

## Nine things worth remembering

<ul class="dc-points" style="font-size: 0.95em;">
  <li>The file system is <b>one tree</b> rooted at <code>/</code>; your working directory decides how relative paths resolve.</li>
  <li><code>pwd</code>, <code>ls</code>, <code>cd</code> answer where you are, what is here, how to move — check before you act.</li>
  <li><code>mkdir</code>, <code>cp</code>, <code>mv</code>, <code>rm</code> organize the tree; <code>rm</code> has <b>no undo</b>.</li>
  <li>Every program has three streams: <code>stdin</code>, <code>stdout</code>, <code>stderr</code>.</li>
  <li>Results on <code>stdout</code>, messages on <code>stderr</code> — that separation is what makes composition safe.</li>
  <li><code>&gt;</code> and <code>&gt;&gt;</code> send output to a file; <code>&lt;</code> feeds input from one; <code>|</code> connects one program to the next.</li>
  <li>A repeated pipeline belongs in a script: hash-bang plus <code>chmod +x</code>.</li>
  <li>Permissions answer <b>who may do what</b>: read, write, execute for owner, group, others.</li>
  <li><code>sys.argv</code>, exit status, and <code>pathlib</code> are the same ideas, seen from inside Python.</li>
</ul>
