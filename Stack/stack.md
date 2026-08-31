# Stack

A stack is just a list you only touch at one end — `append` to push, `pop` to remove the most recent thing. That sounds too simple to build a section around, but the stack is the right tool for a surprisingly deep idea: *"I need to remember things in the order I saw them, and resolve them in reverse."* Whenever a problem involves matching pairs, undoing recent work, or "find the next element that's bigger/smaller than this one," a stack is almost certainly the move. The whole section is about recognizing that shape.

## The core structure

In Python you don't need a special class — a plain list *is* a stack:

```python
stack = []
stack.append(x)     # push
top = stack[-1]      # peek (don't remove)
x = stack.pop()      # pop (LIFO — last in, first out)
```

The only rules: you always add and remove from the same end (`[-1]`), and you never index into the middle. That LIFO discipline — last in, first out — is what makes a stack model "most recent first."

## The single most important mental habit: "does the most recent unresolved thing decide what happens next?"

Before reaching for a stack, ask: "When I process the current element, is the thing it interacts with the *most recently seen* one that hasn't been dealt with yet?"

If yes, that's a stack. A closing bracket must match the *most recent* unmatched opening bracket. A warmer temperature resolves the *most recent* colder day still waiting for a warmer one. An operator in RPN consumes the *two most recent* operands. Every time the answer is "the latest thing I haven't finished with," you push while you're unsure and pop the moment the current element resolves what's on top.

## The two big patterns

**Matching / balancing.** Push openers; when you hit a closer, pop and check it matches. If the stack is empty at the end, everything paired up.

```python
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
for c in s:
    if c in pairs:                        # a closer
        if not stack or stack.pop() != pairs[c]:
            return False
    else:                                 # an opener
        stack.append(c)
return not stack
```

**Monotonic stack ("next greater / next smaller").** This is the pattern that makes the stack section click. You keep the stack in sorted order (increasing or decreasing); before pushing the current element, you *pop everything that the current element resolves*. The classic use: "for each element, find the next one to its right that's bigger."

```python
stack = []                                # holds indices, values increasing bottom->top
result = [0] * len(temps)
for i, t in enumerate(temps):
    while stack and temps[stack[-1]] < t:
        j = stack.pop()                   # t is the "next warmer" for day j
        result[j] = i - j
    stack.append(i)
return result
```

The insight: when you pop `j`, you've found `j`'s answer *for free*, because the current element is the first thing bigger than it that you've encountered. Daily Temperatures, Car Fleet, and Largest Rectangle in Histogram are all monotonic-stack problems wearing different costumes.

## Techniques you'll reuse

**Store indices, not values, when you need distances.** Daily Temperatures needs `i - j`, so the stack holds indices and you look up `temps[i]` when comparing. Largest Rectangle does the same to compute widths.

**Process in a deliberate order.** Car Fleet isn't obviously a stack problem until you sort cars by starting position (descending) and walk them — each car either joins the fleet ahead (gets absorbed) or forms a new fleet, which is exactly a stack of fleet arrival-times where you pop/merge when a car is slower.

**A stack can carry auxiliary info alongside the value.** Min Stack keeps, at each level, both the pushed value *and* the minimum of everything at or below it — so `getMin` is O(1) because the current minimum is always sitting right on top.

**Recursion uses the call stack — so "generate all" problems belong here too.** Generate Parentheses is really backtracking (an explicit stack of choices), included in this section because the balance rule — you can only add `)` when open count exceeds close count — is a stack-validity invariant.

## Pattern groups in NeetCode 150's stack section

1. **Matching / balancing** — Valid Parentheses. Push openers, pop-and-check on closers, empty stack at the end means valid.
2. **Stack with augmented state** — Min Stack. Each entry remembers the running minimum so `push`/`pop`/`top`/`getMin` are all O(1). (This is a class-design problem, not a one-off function.)
3. **Evaluation with a stack of operands** — Evaluate Reverse Polish Notation. Push numbers; on an operator, pop the top two, apply, push the result. The stack *is* the running computation.
4. **Backtracking / balance-constrained generation** — Generate Parentheses. Build strings by choosing `(` or `)` under the invariant that closes never exceed opens.
5. **Monotonic stack (next-greater family)** — Daily Temperatures, Car Fleet, Largest Rectangle in Histogram. Keep a sorted stack; pop everything the current element resolves, computing each popped item's answer as it leaves. This is the section's real payload.

## Suggested order to attack them

1. Valid Parentheses (the canonical push/pop match)
2. Min Stack (stack with extra bookkeeping — a design problem)
3. Evaluate Reverse Polish Notation (stack as a calculator)
4. Generate Parentheses (balance invariant + backtracking)
5. Daily Temperatures (your first monotonic stack — the "answer on pop" insight)
6. Car Fleet (a monotonic stack hiding behind a sort)
7. Largest Rectangle in Histogram (the boss — monotonic stack computing widths on pop)

By the time you reach Largest Rectangle in Histogram, the "pop resolves the popped element's answer" idea from Daily Temperatures will be the thing that makes the width computation make sense instead of looking like magic.

One practical tip: when you suspect a monotonic stack, write a comment stating the invariant before coding — e.g. `# stack holds indices, temps increasing from bottom to top` — and then, for the pop step, write what the answer *is* at the moment you pop. Naming what a pop means is the whole trick of this section.
