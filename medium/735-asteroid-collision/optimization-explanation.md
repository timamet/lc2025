# When the Early Termination Optimization is Needed

## The Optimization Code
```python
# Optimization: Early termination if no collisions possible
if not stack or stack[-1] < 0:
    stack.append(a)
    continue
```

## Two Specific Cases Where This Optimization Kicks In:

### Case 1: Empty Stack (`not stack`)
**When:** Processing a left-moving asteroid when the stack is empty
**Why:** No previous asteroids exist, so no collisions are possible
**Example:**
```
Input: [-5, -3, -1]
Processing -5: Stack is [], no collision possible
→ Add -5 directly to stack
```

### Case 2: Stack Top is Left-Moving (`stack[-1] < 0`)
**When:** Processing a left-moving asteroid when the most recent asteroid is also left-moving
**Why:** Two left-moving asteroids will never collide (same direction)
**Example:**
```
Input: [1, -2, -3, -4]
Processing -2: Collides with 1, result depends on sizes
Processing -3: Stack top is -2 (left-moving), no collision possible
Processing -4: Stack top is -3 (left-moving), no collision possible
```

## Visual Examples:

### ✅ Optimization Case 1 - Empty Stack
```
Step 1: [-5] → Stack: []
        ←5   (no other asteroids to collide with)
        Result: Add -5 directly
```

### ✅ Optimization Case 2 - Both Moving Left
```
Stack: [←3, ←2]  New: ←4
       ←3  ←2    ←4
       (no collision - all moving same direction)
       Result: Add -4 directly
```

### ❌ No Optimization - Collision Possible
```
Stack: [→3]  New: ←4
       →3    ←4
       (collision will occur - need to process)
```

## Performance Benefits:

1. **Skip unnecessary while loop**: Avoids entering the collision detection loop when no collisions are possible
2. **Early termination**: Immediately adds the asteroid and continues to the next one
3. **Common case optimization**: Many real-world scenarios have sequences of same-direction asteroids

## Code Without Optimization:
```python
# Without optimization - always enters collision loop
while stack and stack[-1] > 0:  # This would be false immediately
    # ... collision logic never executes
else:
    stack.append(a)  # Always executes this branch
```

## Code With Optimization:
```python
# With optimization - skip the loop entirely
if not stack or stack[-1] < 0:
    stack.append(a)  # Direct addition, skip all collision logic
    continue
```

## When It Matters Most:
- **Input patterns**: `[-1, -2, -3, -4, -5]` (all left-moving)
- **Mixed patterns**: `[1, 2, -1, -2, -3]` (after collisions, remaining left-moving asteroids)
- **Large inputs**: More significant performance improvement with larger arrays

The optimization is particularly valuable because it handles very common cases (empty stack and same-direction sequences) with minimal code complexity while providing measurable performance improvements.
