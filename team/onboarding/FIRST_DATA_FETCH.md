# First data fetch: a step-by-step guide for non-technical owners

This guide shows how to prove that your MEL team can fetch real data, safely and in a small way, before you turn on any daily schedule.

It is written for the person who owns the team (the **Owner**). Some steps are done by you, some by the **Lead chat** (the Claude chat where you talk to your MEL Lead). Each step says who does it.

**Words used here**

- **Source:** a public website or data service the team reads from. All sources are listed in the file `data/sources.yml`.
- **Collector:** the agent that adds sources to that list and checks the results.
- **Actions:** GitHub's built-in robot. It does the actual downloading when you press a button.
- **Board:** the folder `team/board/` where agents and you leave messages for each other.

## Before you start

- Your instance repo exists on GitHub and its Actions and Pages settings are done (see `team/SETUP_STATUS.md`).
- The Collector has added your sources to `data/sources.yml`. Right now they should all say `enabled: false` (off).
- The Lead chat can read your repo.

## Why start small

Three reasons.

1. **Every download is saved in the repo.** A large, unfiltered download makes the repo heavy. Start with filtered downloads.
2. **A green tick in Actions does not prove data arrived.** The tool carries on if a source fails. You must read the log lines to see `OK` or `FAIL`.
3. **Licences are not confirmed yet.** Nothing should be published until each source's terms are read on the publisher's own page.

## Part A: Authorise a small test

1. **[Owner]** Tell the Lead chat what to test. Say which sources are in, and which are out (for example a source that needs a password-like key, or one that is very large). Say how narrow the first test should be (for example, a few cities only).
2. **[Lead chat]** Records your decision on the board as a message from you, addressed to the Collector. It lists what may be switched on, with limits, and what must stay off.
3. **[Owner]** Open the **Collector** scheduled task in Claude and click **Run now**. Wait until it says it finished.
4. **[Owner]** Tell the Lead chat "ran".
5. **[Lead chat]** Checks `data/sources.yml` on the `main` branch and tells you which sources are now on, which stayed off, and why.

## Part B: Run the fetch

6. **[Owner]** Open your repo's Actions page: `https://github.com/<owner>/<repo>/actions`
7. In the left list click **Fetch transform dashboard**.
8. Click **Run workflow** on the right. Keep the branch as **main**. Click the green **Run workflow** button.
9. Wait one to two minutes, then refresh the page. A green tick means the job finished. It does not yet mean data arrived.

## Part C: Check the result

10. **[Owner]** Click the run, click **Pipeline**, and open the step called **Fetch enabled sources**. You will see one line per source:
    - `OK <name>` means data arrived.
    - `FAIL <name>` means it did not. The line gives a reason. Copy it and send it to the Lead chat.
11. **[Owner]** Tell the Lead chat "fetched".
12. **[Lead chat]** Checks the `main` branch: the status file shows a success time for each source that worked, the files in `data/raw/` are small, and the dashboard data updated. It reports the result to you.

## Part D: Before anything is public

13. **[Owner and Lead chat]** For every source that worked, read its licence on the publisher's own page and record it on the board. If the terms do not allow reuse, switch the source back off.
14. **[Owner]** Decide whether to turn on the daily automatic fetch. Until you do, the fetch only runs when you click **Run workflow**.

## If something goes wrong

| What you see | What to do |
|---|---|
| No **Run workflow** button | Check that Actions is enabled in the repo's Settings, then tell the Lead chat |
| Every source says `FAIL` | Tell the Lead chat. It may mean the data hosts block GitHub's robot, and we would need a different plan |
| A run is red | Copy the error text to the Lead chat. Do not re-run again and again |
| A green tick but no data | Read the `OK`/`FAIL` lines in Part C. Green alone proves nothing |

## What not to do

- Do not paste passwords or API keys into the repo or into the Lead chat.
- Do not turn on the daily schedule until Part D is finished.
- Do not switch on very large sources without a filter.
