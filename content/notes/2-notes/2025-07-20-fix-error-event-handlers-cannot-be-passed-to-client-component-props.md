---
Title: "Fix Error: Event handlers cannot be passed to Client Component props."
Published: 2025-07-20
author: Sumit Patel
description: "Note:"
tags: ["next"]
---

  Note: 

  The Challenge:
[--more--]
```
 ⨯ Error: Event handlers cannot be passed to Client Component props.
  <button onClick={function onClick} className=... children=...>
                  ^^^^^^^^^^^^^^^^^^

If you need interactivity, consider converting part of this to a Client Component.
    at stringify (<anonymous>)
    at stringify (<anonymous>)
digest: "3510721672"
```


  I encountered a persistent and misleading error in a Next.js 14 application: Error: Event handlers cannot be passed to Client Component props. The error occurred when
  navigating to a dynamic user profile page (/app/[username]), but the stack trace was generic and didn't point to a specific component.

  The Debugging Journey:


  The initial debugging process was a long chase, as the error message suggested a common but incorrect root cause in this case. My attempts included:


   1. Standard Checks: Ensured all components using client-side hooks (like useState, useEffect, useRouter) were correctly marked with the "use client"; directive. This fixed
       several minor bugs but not the main error.
   2. Refactoring: Broke down large client components into smaller, more manageable ones, thinking the issue was related to component complexity. This improved code quality
      but didn't solve the problem.
   3. Data Fetching: Investigated and fixed an unrelated SSL error in the server-side fetch call within the page.js file.
   4. Cache Clearing: Completely cleared the Next.js cache (.next directory) to rule out stale build artifacts.
   5. The Breakthrough: After exhausting all conventional methods, I decided to investigate the project's recent git history to isolate the exact commit that introduced the
      bug.

  The Root Cause & The Solution:


  The git show <commit_hash> command revealed that the problematic commit had introduced a new file: app/[username]/not-found.js.


  This file is a special Next.js convention for rendering a 404 page for the /[username] route. The file contained a button with an onClick handler to allow users to go
  back. However, like all components in the App Router, it was a Server Component by default.


  The error was only triggered when visiting a non-existent user profile, which is why it was so hard to trace. The server-side rendering process for the 404 page failed
  because it encountered an onClick handler, which is client-side interactivity.


  The fix was a simple, one-line change: adding "use client"; to the top of app/[username]/not-found.js.

  Key Takeaways:


   * The error isn't always on the "happy path": The bug was in an error-handling file (not-found.js), not the main page component. It's crucial to debug edge cases and
     special files.
   * Next.js conventions are still components: Special files like layout.js, error.js, and not-found.js must adhere to the same Server/Client Component rules as any other
     component.
   * `git` is a powerful debugging tool: When you're stuck, using git log, git show, or git bisect to trace the history of a bug can be the most effective way to find its
     origin.
   * Generic errors can be misleading: The error message pointed to a symptom, not the cause. The real issue was a server component trying to render client-side interactive
     elements.
