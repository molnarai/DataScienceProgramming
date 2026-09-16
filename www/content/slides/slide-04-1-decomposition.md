+++
title = "Decomposition"
description = "Breaking a large problem into smaller pieces: tasks, steps, and the four payoffs of clarity, reuse, checking, and collaboration"
weight = 41
outputs = ["Reveal"]
math = false
thumbnail = "/imgs/Programming_Function_Coding_Contract.png"

[reveal_hugo]
custom_theme = "css/reveal-robinson.css"
slide_number = true
transition = "none"

+++

<style>
  .reveal .slides section { box-sizing: border-box; }
  .reveal .dc-sub { color: #666; font-size: 0.9em; }
  .reveal .dc-kicker { color: #CC0000; font-size: 0.55em; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin: 0 0 4px 0; }
  .reveal .dc-lead { font-size: 1.05em; }
  .reveal .dc-small { font-size: 0.75em; }
  .reveal .dc-muted { color: #666; }

  /* Goal → tasks → steps tree */
  .reveal .dc-goal { display: table; margin: 8px auto 0 auto; padding: 8px 22px; background: #003478; color: #fff; border-radius: 6px; font-weight: 700; font-size: 0.8em; }
  .reveal .dc-tasks { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 22px; position: relative; }
  .reveal .dc-tasks::before { content: ""; position: absolute; top: -14px; left: 8%; right: 8%; border-top: 2px solid #003478; }
  .reveal .dc-task { box-sizing: border-box; flex: 1 1 0; min-width: 150px; background: #f4f6f9; border-top: 4px solid #003478; border-radius: 4px; padding: 8px 10px; font-size: 0.58em; position: relative; }
  .reveal .dc-tasks.wrap .dc-task { flex: 0 1 30%; }
  .reveal .dc-task::before { content: ""; position: absolute; top: -16px; left: 50%; height: 12px; border-left: 2px solid #003478; }
  .reveal .dc-task h4 { font-size: 1.1em; margin: 0 0 6px 0; }
  .reveal .dc-task ul { margin: 0 0 0 1.1em; }
  .reveal .dc-task li { margin-bottom: 0.15em; }

  /* Card grid */
  .reveal .dc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px; }
  .reveal .dc-card { background: #f4f6f9; border-left: 5px solid #003478; padding: 10px 16px; border-radius: 4px; }
  .reveal .dc-card h3 { margin: 0 0 4px 0; font-size: 0.95em; }
  .reveal .dc-card p { margin: 0; font-size: 0.72em; }
  .reveal .dc-card.red { border-left-color: #CC0000; }
  .reveal .dc-card.red h3 { color: #CC0000; }

  /* Horizontal flow */
  .reveal .dc-flow { display: flex; align-items: center; justify-content: center; flex-wrap: wrap; gap: 6px; margin: 14px 0; }
  .reveal .dc-node { background: #f4f6f9; border: 2px solid #003478; border-radius: 6px; padding: 8px 10px; font-size: 0.58em; text-align: center; max-width: 150px; }
  .reveal .dc-node.dark { background: #003478; color: #fff; }
  .reveal .dc-node.red { border-color: #CC0000; }
  .reveal .dc-arrow { color: #003478; font-size: 0.9em; font-weight: 700; }
  .reveal .dc-flow.tight { flex-wrap: nowrap; gap: 4px; }
  .reveal .dc-flow.tight .dc-node { max-width: 112px; font-size: 0.5em; padding: 6px 6px; }
  .reveal .dc-stack { display: flex; flex-direction: column; gap: 6px; }

  /* Payoff lines */
  .reveal .dc-payoffs { list-style: none; margin: 10px 0 0 0; }
  .reveal .dc-payoffs li { font-size: 0.8em; margin-bottom: 0.55em; padding-left: 0.2em; }
  .reveal .dc-payoffs b { color: #003478; display: inline-block; min-width: 7.6em; }

  /* Owners */
  .reveal .dc-owners { display: grid; grid-template-columns: auto 40px auto; gap: 8px 6px; align-items: center; justify-content: center; margin-top: 14px; }
  .reveal .dc-owners .dc-node { max-width: none; font-size: 0.65em; }

  .reveal .dc-steps { counter-reset: s; list-style: none; margin: 10px 0 0 0; }
  .reveal .dc-steps li { counter-increment: s; font-size: 0.8em; margin-bottom: 0.5em; padding-left: 2.2em; position: relative; }
  .reveal .dc-steps li::before { content: counter(s); position: absolute; left: 0; top: 0; width: 1.5em; height: 1.5em; line-height: 1.5em; text-align: center; border-radius: 50%; background: #003478; color: #fff; font-size: 0.85em; font-weight: 700; }
  .reveal .dc-success { margin: 18px auto 0 auto; width: 85%; padding: 18px 24px; background: #003478; color: #fff; border-radius: 8px; font-size: 0.85em; line-height: 1.35; text-align: center; }
  .reveal .dc-node.e4 { max-width: 150px; font-size: 0.55em; }
  .reveal .dc-owner { margin-top: 6px; font-size: 0.85em; font-style: italic; color: #CC0000; }
  .reveal .dc-node.dark .dc-owner { color: #fff; }
  .reveal .dc-levels { font-size: 0.55em; margin-top: 10px; width: 100%; }
  .reveal .dc-levels td { vertical-align: top; }
  .reveal .dc-levels td:first-child b { color: #003478; }
  .reveal .dc-levels th:nth-child(2) { width: 34%; }
</style>

<p class="dc-kicker">IFI 8410 — Session 4: Functions and Decomposition</p>
<h1>Decomposition</h1>
<p class="dc-sub">Breaking a large problem into smaller pieces</p>

{{% note %}}
Before we write a single function today, we look at the design activity that decides what the functions should be. None of the examples in this deck involve code on purpose: decomposition is a way of thinking, and it is easier to see when syntax is not in the way.
{{% /note %}}

***

<p class="dc-kicker">The problem</p>

## Why large goals feel hard

<p class="dc-lead">"Organize an event." "Complete a study." "Improve a service."</p>

<p>A large goal is hard not because it is big, but because many things are <b>mixed together</b>:</p>

<ul>
  <li class="fragment">decisions that have not been made yet</li>
  <li class="fragment">dependencies — what has to happen first</li>
  <li class="fragment">uncertainty about what "done" even looks like</li>
</ul>

<p class="fragment" style="margin-top: 30px;">You cannot act on a goal. You can only act on a <b>next step</b>.</p>

{{% note %}}
Ask the class: what is the first thing you would do if told to "improve customer retention"? Most answers will be a sub-goal, not an action — that is the point.
{{% /note %}}

***

<p class="dc-kicker">Definition</p>

## Decomposition

<blockquote style="font-size: 1em; width: 90%;">
Taking a large goal and dividing it into smaller, understandable <b>tasks</b> and <b>steps</b>.
</blockquote>

<p>It does <b>not</b> make the goal less important or change its purpose.</p>

<p>It makes the work <b>visible</b> — people can see:</p>

<ul>
  <li>what needs to happen</li>
  <li>in what order</li>
  <li>who is responsible</li>
  <li>how each completed piece contributes to the whole</li>
</ul>

***

<p class="dc-kicker">Structure</p>

## Goal → tasks → steps

<div class="dc-goal">Large goal</div>
<div class="dc-tasks">
  <div class="dc-task"><h4>Task 1</h4><ul><li>Step 1</li><li>Step 2</li></ul></div>
  <div class="dc-task"><h4>Task 2</h4><ul><li>Step 1</li><li>Step 2</li></ul></div>
  <div class="dc-task"><h4>Task 3</h4><ul><li>Step 1</li><li>Step 2</li></ul></div>
</div>

<p style="margin-top: 36px;">Focus on <b>one meaningful task at a time</b> — while keeping sight of the overall outcome.</p>

***

<p class="dc-kicker">Why break work down?</p>

## Not a longer to-do list

<p>The goal is a plan people can <b>understand, use, inspect, and improve</b>.</p>

<div class="dc-grid">
  <div class="dc-card"><h3>Clarity</h3><p>Vague goals become concrete actions; dependencies become visible.</p></div>
  <div class="dc-card"><h3>Reuse</h3><p>A proven approach is kept and adapted instead of rebuilt from nothing.</p></div>
  <div class="dc-card"><h3>Checking</h3><p>Progress and quality are reviewed piece by piece — not only at the end.</p></div>
  <div class="dc-card"><h3>Collaboration</h3><p>Work is shared without everyone managing the whole effort.</p></div>
</div>

{{% note %}}
These four words come back on every example slide, and again at the end when we map them onto Python functions. Worth writing them on the board.
{{% /note %}}

***

<p class="dc-kicker">Payoff 1 of 4</p>

## Clarity

<p>Each task has a recognizable purpose; each step moves the work forward.</p>

<ul>
  <li>Separates what is <b>done</b> from what is still <b>uncertain</b></li>
  <li>Reveals <b>dependencies</b></li>
</ul>

<div class="dc-flow" style="margin-top: 40px;">
  <div class="dc-node">Choose a venue</div>
  <div class="dc-arrow">→</div>
  <div class="dc-node">Send invitations<br><span class="dc-muted">(they need the location)</span></div>
</div>

***

<p class="dc-kicker">Payoff 2 of 4</p>

## Reuse

<p>Many large efforts contain tasks you will need again:</p>

<ul>
  <li>planning a meeting</li>
  <li>reviewing information</li>
  <li>approving a request</li>
  <li>preparing materials</li>
</ul>

<p style="margin-top: 30px;">Reuse is <b>not</b> repeating work without thought.<br>
It is <b>preserving a proven approach</b> so people can adapt it rather than start from nothing.</p>

***

<p class="dc-kicker">Payoff 3 of 4</p>

## Checking

<p>Small tasks can be reviewed <b>before</b> the whole effort is complete — so a serious problem does not surface at the very end.</p>

<p>At each piece, ask:</p>

<ul>
  <li class="fragment">Is this step complete?</li>
  <li class="fragment">Does it meet the expected standard?</li>
  <li class="fragment">Is important information missing?</li>
  <li class="fragment">Does the next task have what it needs to begin?</li>
</ul>

***

<p class="dc-kicker">Payoff 4 of 4</p>

## Collaboration

<p class="dc-small">Works best when each task has a <b>clear outcome</b>, a <b>responsible owner</b>, and a <b>known connection</b> to other tasks.</p>

<div class="dc-owners">
  <div class="dc-node dark">Planning task</div><div class="dc-arrow">→</div><div class="dc-node">Person or group A</div>
  <div class="dc-node dark">Preparation task</div><div class="dc-arrow">→</div><div class="dc-node">Person or group B</div>
  <div class="dc-node dark">Review task</div><div class="dc-arrow">→</div><div class="dc-node">Person or group C</div>
  <div class="dc-node dark">Final delivery task</div><div class="dc-arrow">→</div><div class="dc-node">Person or group D</div>
</div>

<p class="dc-small" style="margin-top: 20px;">Fewer duplicated efforts, missed handoffs, and "who acts next?" moments.</p>

***

<p class="dc-kicker">How to do it</p>

## A practical process

<ol class="dc-steps">
  <li class="fragment">Describe the <b>final outcome</b> clearly — start there, not with activities.</li>
  <li class="fragment">Identify the <b>major tasks</b> needed to produce that outcome.</li>
  <li class="fragment">Divide each task into steps — <b>only until the next action is clear</b>.</li>
  <li class="fragment">Put tasks in order and mark <b>dependencies</b>.</li>
  <li class="fragment">Assign <b>responsibility</b> and agree how each result will be <b>checked</b>.</li>
  <li class="fragment"><b>Review</b> the plan as work progresses; adjust when new information appears.</li>
</ol>

***

<p class="dc-kicker">How far to go?</p>

## The right level of detail

<div class="dc-grid">
  <div class="dc-card red">
    <h3>Too broad</h3>
    <p>People do not know what to do next.</p>
    <p style="margin-top: 8px;"><i>"Handle the logistics."</i></p>
  </div>
  <div class="dc-card red">
    <h3>Too narrow</h3>
    <p>A distracting list of tiny actions that no longer helps anyone understand the work.</p>
    <p style="margin-top: 8px;"><i>"Open the fridge. Take out the butter."</i></p>
  </div>
</div>

<p style="margin-top: 36px; text-align: center;">Stop dividing when <b>the next action is obvious</b>.</p>

***

<p class="dc-kicker">Example 1 — simple</p>

## Hosting a dinner

<p class="dc-small dc-muted">Host a dinner for several friends on Saturday evening.</p>

<div class="dc-goal">Host a dinner</div>
<div class="dc-tasks">
  <div class="dc-task"><h4>Plan the meal</h4><ul><li>Ask guests about dietary needs</li><li>Choose dishes</li><li>Make a shopping list</li></ul></div>
  <div class="dc-task"><h4>Prepare for guests</h4><ul><li>Confirm who is attending</li><li>Set the table</li><li>Prepare drinks and seating</li></ul></div>
  <div class="dc-task"><h4>Prepare the food</h4><ul><li>Shop for ingredients</li><li>Prepare items that can be made early</li><li>Cook and serve the meal</li></ul></div>
</div>

<p class="dc-small" style="margin-top: 24px;">Avoids: buying ingredients too late · more food than fits on the stove · learning about a dietary restriction <i>after</i> choosing the menu.</p>

***

<p class="dc-kicker">Example 1 — simple</p>

## Dinner: the four payoffs

<ul class="dc-payoffs">
  <li><b>Clarity</b> "Host a dinner" is planning, preparation, and serving — not one undefined activity.</li>
  <li><b>Reuse</b> Keep a meal-planning checklist and adapt it for the next dinner.</li>
  <li><b>Checking</b> Review the guest list, shopping list, and table before cooking begins.</li>
  <li><b>Collaboration</b> One person shops, another prepares a dish, another sets the table.</li>
</ul>

***

<p class="dc-kicker">Example 2 — medium</p>

## Organizing a student workshop

<div class="dc-goal">Organize a one-day student workshop</div>
<div class="dc-tasks wrap">
  <div class="dc-task"><h4>Define the workshop</h4><ul><li>Choose topic and audience</li><li>Set learning goals</li><li>Decide date and length</li></ul></div>
  <div class="dc-task"><h4>Arrange logistics</h4><ul><li>Reserve a room or online space</li><li>Confirm presenters and support</li><li>Prepare accessibility arrangements</li></ul></div>
  <div class="dc-task"><h4>Communicate</h4><ul><li>Create an announcement</li><li>Open registration</li><li>Send reminders and details</li></ul></div>
  <div class="dc-task"><h4>Prepare the session</h4><ul><li>Create activities and materials</li><li>Prepare equipment and handouts</li><li>Review the schedule</li></ul></div>
  <div class="dc-task"><h4>Run and review</h4><ul><li>Welcome participants</li><li>Deliver activities, take questions</li><li>Collect feedback</li><li>Record improvements</li></ul></div>
</div>

***

<p class="dc-kicker">Example 2 — medium</p>

## The same plan as a flow of results

<p>Tasks have <b>dependencies</b>: each stage produces what the next one needs.</p>

<div class="dc-flow tight" style="margin-top: 40px;">
  <div class="dc-node">Topic and goals</div><div class="dc-arrow">→</div>
  <div class="dc-node">Date, location, presenters</div><div class="dc-arrow">→</div>
  <div class="dc-node">Participant communication</div><div class="dc-arrow">→</div>
  <div class="dc-node">Materials and final schedule</div><div class="dc-arrow">→</div>
  <div class="dc-node dark">Workshop day</div><div class="dc-arrow">→</div>
  <div class="dc-node">Feedback and improvement</div>
</div>

<p class="dc-small" style="margin-top: 36px;">A tree shows <i>what</i> the work is. A flow shows <i>what each piece hands to the next</i>.</p>

{{% note %}}
The flow view is exactly how a data pipeline reads: load, clean, transform, summarize, report. Each stage's output is the next stage's input.
{{% /note %}}

***

<p class="dc-kicker">Example 2 — medium</p>

## Workshop: the four payoffs

<ul class="dc-payoffs">
  <li><b>Clarity</b> Not just "an event to schedule": purpose, logistics, communication, materials, and review are separate work.</li>
  <li><b>Reuse</b> The plan becomes a template — registration messages, accessibility checks, feedback questions, timeline.</li>
  <li><b>Checking</b> Confirm the room, match materials to learning goals, verify participants got the details, examine feedback.</li>
  <li><b>Collaboration</b> Content, registration, and room/equipment can each go to a different group — with clear handoffs.</li>
</ul>

***

<p class="dc-kicker">Example 3 — complex</p>

## Improving community flood preparedness

<div class="dc-goal">Prepare for, respond to, and recover from flooding</div>
<div class="dc-tasks wrap">
  <div class="dc-task"><h4>Understand risks and needs</h4><ul><li>Identify flood-prone areas</li><li>Review past flood impacts</li><li>Identify people needing extra support</li></ul></div>
  <div class="dc-task"><h4>Set priorities, prepare plan</h4><ul><li>Define desired outcomes</li><li>Choose actions by urgency and impact</li><li>Estimate resources and funding</li></ul></div>
  <div class="dc-task"><h4>Improve physical readiness</h4><ul><li>Inspect drainage and structures</li><li>Identify repair work</li><li>Prepare supplies and access routes</li></ul></div>
  <div class="dc-task"><h4>Communication and response</h4><ul><li>Define warnings and channels</li><li>Prepare evacuation and shelter</li><li>Practice with relevant groups</li></ul></div>
  <div class="dc-task"><h4>Recovery and improvement</h4><ul><li>Document impacts</li><li>Coordinate recovery support</li><li>Review what worked and failed</li><li>Update the plan</li></ul></div>
</div>

{{% note %}}
Complex because it affects many people, conditions keep changing, and it spans infrastructure, communication, emergency response, vulnerable residents, funding, and long-term learning. No single person or group can do it alone.
{{% /note %}}

***

<p class="dc-kicker">Example 3 — complex</p>

## Different timing, still connected

<div class="dc-flow" style="margin-top: 30px;">
  <div class="dc-stack">
    <div class="dc-node">Risk information</div>
    <div class="dc-node">Community needs</div>
    <div class="dc-node">Available resources</div>
  </div>
  <div class="dc-arrow">→</div>
  <div class="dc-node dark">Priorities and plan</div><div class="dc-arrow">→</div>
  <div class="dc-node">Action schedule</div><div class="dc-arrow">→</div>
  <div class="dc-node">Preparedness actions</div>
</div>

<div class="dc-flow">
  <div class="dc-node red">Flood event or practice</div><div class="dc-arrow">→</div>
  <div class="dc-node">Review results</div><div class="dc-arrow">→</div>
  <div class="dc-node">Update future actions</div>
  <div class="dc-arrow">↺</div>
</div>

<p class="dc-small" style="margin-top: 24px;">Several inputs <b>converge</b>; real events feed a <b>loop</b> that updates the plan.</p>

***

<p class="dc-kicker">Example 3 — complex</p>

## Flood plan: the four payoffs

<ul class="dc-payoffs">
  <li><b>Clarity</b> "Be better prepared" is too broad to guide decisions; the tasks separate risk, priorities, readiness, communication, response, and learning.</li>
  <li><b>Reuse</b> Warning messages, contact lists, shelter procedures, and assessment forms are maintained — not recreated mid-emergency.</li>
  <li><b>Checking</b> Verify risk data, inspect repairs, test warnings, review drills, update after every event.</li>
  <li><b>Collaboration</b> Leaders, emergency services, infrastructure, health, schools, residents, businesses — each owns a part and a handoff.</li>
</ul>


***

<!-- Begin Example 4 -->
<p class="dc-kicker">Example 4 — working backward</p>

## Start from the finish line

<p>Examples 1–3 went <b>top-down</b>: name the goal, split it into tasks.</p>
<p>Step 1 of our process said: <i>describe the final outcome clearly — start there, not with activities.</i> Now take that literally.</p>

<div class="dc-grid" style="margin-top: 26px;">
  <div class="dc-card"><h3>Forward</h3><p>"What do we do first?"<br>→ easy to start busy work that leads nowhere</p></div>
  <div class="dc-card red"><h3>Backward</h3><p>"What does <b>done</b> look like?"<br>← "What had to be finished just before that?"</p></div>
</div>

{{% note %}}
Working backward is how analysts should plan a data project too: start from the report or decision the stakeholder needs, then ask which numbers it needs, which cleaned data those need, and which raw sources that needs.
{{% /note %}}

***

<!-- Class Activity -->

<p class="dc-kicker">Your turn — Example 4</p>

## Plan a quarterly insights brief — backward

<p>Your team publishes a <b>quarterly industry insights brief</b>: an analysis of the latest industry data, written up for stakeholders.</p>

<div class="dc-success" style="font-size: 0.72em; margin-bottom: 20px;">
  <b>Done means:</b> a finalized, verified brief delivered to stakeholders — with clear analytical takeaways and a way to collect reader feedback.
</div>

<ol class="dc-steps">
  <li>Start from <b>done</b>. Ask: <i>what had to be finished just before this?</i> Repeat until you reach the start.</li>
  <li>Name the <b>major tasks</b> you found — and who would own each.</li>
  <li>Break each task into <b>steps</b>, stopping when the next action is clear.</li>
  <li>Mark one <b>checkpoint</b> and one <b>handoff</b> between people.</li>
</ol>

<p class="dc-small dc-muted" style="text-align: center;">LiveSythesis · 10 minutes</p>

{{% note %}}
Do not show the next slides until groups report back. Collect their major tasks on the board in the order they found them (backward), then compare with the solution: D Scoping & data → C Analysis → B Production & review → A Delivery & feedback.
{{% /note %}}

***

{{< slide auto-animate="" >}}

<p class="dc-kicker">Example 4 — working backward</p>

## The quarterly insights brief

<p>First, define success <b>in plain language</b>:</p>

<div class="dc-success" data-id="e4-outcome">
  A finalized, verified quarterly brief delivered to stakeholders — with clear analytical takeaways and a feedback mechanism in place.
</div>

<p class="dc-small dc-muted" style="margin-top: 26px;">Not "write a report." A description of the finished state that anyone can check against.</p>

***

{{< slide auto-animate="" >}}

<p class="dc-kicker">Example 4 — Level 1: major tasks</p>

## Walk backward from the outcome

<p class="dc-small">Ask repeatedly: <b>what had to be finished just before this?</b></p>

<div class="dc-flow" style="margin-top: 30px; flex-wrap: nowrap; gap: 4px;">
  <div class="fragment" data-fragment-index="4" style="display: flex; align-items: center; gap: 4px;">
    <div class="dc-node e4" data-id="e4-d"><b>D</b> Scoping &amp; data gathering<div class="dc-owner">Research team</div></div><div class="dc-arrow">→</div>
  </div>
  <div class="fragment" data-fragment-index="3" style="display: flex; align-items: center; gap: 4px;">
    <div class="dc-node e4" data-id="e4-c"><b>C</b> Data analysis &amp; insights<div class="dc-owner">Data team</div></div><div class="dc-arrow">→</div>
  </div>
  <div class="fragment" data-fragment-index="2" style="display: flex; align-items: center; gap: 4px;">
    <div class="dc-node e4" data-id="e4-b"><b>B</b> Production &amp; quality review<div class="dc-owner">Editorial</div></div><div class="dc-arrow">→</div>
  </div>
  <div class="fragment" data-fragment-index="1" style="display: flex; align-items: center; gap: 4px;">
    <div class="dc-node e4" data-id="e4-a"><b>A</b> Final delivery &amp; feedback<div class="dc-owner">Communications</div></div><div class="dc-arrow">→</div>
  </div>
  <div class="dc-node dark e4" data-id="e4-outcome">Brief delivered, feedback in place</div>
</div>

<p class="fragment dc-small" data-fragment-index="5" style="margin-top: 26px;">Planned <b>right to left</b> — executed <b>left to right</b>.</p>

{{% note %}}
Reveal the tasks in backward order: A needs a finished, reviewed brief (B); B needs verified findings (C); C needs the right questions and raw data (D). Level 1 alone already gives: clarity (four recognizable phases instead of "publish a brief"), reuse (Scoping → Analysis → Production → Delivery frames every future quarter), checking (a boundary between phases where progress can be evaluated), and collaboration (high-level ownership by team).
{{% /note %}}

***

{{< slide auto-animate="" >}}

<p class="dc-kicker">Example 4 — Level 2: smaller steps</p>

## One level further: next actions

<div class="dc-goal" data-id="e4-outcome">Brief delivered, feedback in place</div>
<div class="dc-tasks">
  <div class="dc-task" data-id="e4-d"><h4>D · Scoping &amp; data</h4><ul><li><b>D1</b> Define research questions and audience</li><li><b>D2</b> Collect raw datasets; interview experts</li></ul><div class="dc-owner">Research team</div></div>
  <div class="dc-task" data-id="e4-c"><h4>C · Analysis &amp; insights</h4><ul><li><b>C1</b> Clean raw data; compute summary metrics</li><li><b>C2</b> Synthesize metrics into findings and trends</li></ul><div class="dc-owner">Data analyst</div></div>
  <div class="dc-task" data-id="e4-b"><h4>B · Production &amp; review</h4><ul><li><b>B1</b> Draft charts and narrative</li><li><b>B2</b> Inspect for accuracy and layout</li><li><b>B3</b> Obtain final sign-off</li></ul><div class="dc-owner">Technical writer, editorial</div></div>
  <div class="dc-task" data-id="e4-a"><h4>A · Delivery &amp; feedback</h4><ul><li><b>A1</b> Send through distribution channels</li><li><b>A2</b> Deploy reader feedback forms</li></ul><div class="dc-owner">Communications</div></div>
</div>

<p class="dc-small dc-muted" style="margin-top: 22px;">Detailed enough to act on — not bogged down in tiny actions like "open the spreadsheet."</p>

***

<p class="dc-kicker">Example 4 — comparing the two levels</p>

## Brief: the four payoffs at two levels

<table class="dc-levels">
  <thead><tr><th></th><th>Level 1 — major tasks</th><th>Level 2 — smaller steps</th></tr></thead>
  <tbody>
    <tr><td><b>Clarity</b></td><td>A vague goal becomes four recognizable phases.</td><td>Shows exactly what is finished and exposes exact dependencies — layout inspection <b>B2</b> must come before sending <b>A1</b>.</td></tr>
    <tr><td><b>Reuse</b></td><td>A standard sequence — Scoping → Analysis → Production → Delivery — frames every future brief.</td><td>Keeps repeatable artifacts: data-cleaning scripts <b>C1</b>, a layout template <b>B1</b>, feedback questions <b>A2</b>.</td></tr>
    <tr><td><b>Checking</b></td><td>Boundaries between phases where progress is evaluated.</td><td>Concrete review points: verify metrics before drafting visuals; inspect layout before publishing.</td></tr>
    <tr><td><b>Collaboration</b></td><td>Ownership by team: Research, Data, Editorial, Communications.</td><td>Explicit handoffs: the analyst finishes <b>C1</b> and hands clean metrics to the writer for <b>B1</b>.</td></tr>
  </tbody>
</table>

<p class="dc-small" style="margin-top: 18px; text-align: center;">Each level adds detail — and each piece still points at the same outcome. That is the final check.</p>

{{% note %}}
Point at C1: "reusable data-cleaning script" is the first time a task in this deck is literally code. Hold that thought for the Python slide. The closing line leads directly into the final-review questions on the next slide.
{{% /note %}}

<!-- End Example 4 -->
***

<p class="dc-kicker">Final review</p>

## Keeping the pieces connected

<table style="font-size: 0.68em; margin-top: 20px;">
  <thead><tr><th>Question</th><th>Protects</th></tr></thead>
  <tbody>
    <tr><td>Is every task connected to the overall goal?</td><td><b>Clarity</b> — no unnecessary work</td></tr>
    <tr><td>Can a useful task or set of steps be used again?</td><td><b>Reuse</b> of successful approaches</td></tr>
    <tr><td>Is there a clear point where each important result is reviewed?</td><td><b>Checking</b> before problems spread</td></tr>
    <tr><td>Does everyone know who is responsible and what they need from others?</td><td><b>Collaboration</b></td></tr>
  </tbody>
</table>

<p style="margin-top: 30px; text-align: center;">Understandable <b>without</b> becoming fragmented.</p>

***

<p class="dc-kicker">From plans to programs</p>

## In Python, the pieces are functions

```python
def load_sales(path):        ...   # one task, one responsibility
def clean(rows):             ...
def summarize(rows):         ...
def format_report(summary):  ...

report = format_report(summarize(clean(load_sales("sales.csv"))))
```

<ul class="dc-payoffs" style="margin-top: 16px;">
  <li><b>Clarity</b> a name and a docstring that state one job</li>
  <li><b>Reuse</b> call it again with different inputs</li>
  <li><b>Checking</b> test each piece with <code>assert</code></li>
  <li><b>Collaboration</b> a contract: parameters in, return value out</li>
</ul>

{{% note %}}
This is the bridge to the rest of the session. Each function returns a value instead of printing, so the next stage — or a test — can use it. That is the "handoff" from the collaboration slide.
{{% /note %}}

***

<p class="dc-kicker">Takeaway</p>

<h2 style="margin-top: 60px;">Small enough to guide action.<br>Connected enough to produce one result.</h2>

<p style="margin-top: 40px;">Next: <a href="../slide-04-2-python-functions-scripts/">Python functions and scripts</a></p>

<p class="dc-small dc-muted" style="margin-top: 40px;">Reading: <a href="../../blog/decomposition/">Decomposition: Breaking a Large Problem into Smaller Pieces</a></p>
