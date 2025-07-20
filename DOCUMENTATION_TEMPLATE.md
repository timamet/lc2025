# LeetCode Problem Documentation Template

## Instructions for Creating Problem Documentation

Use this template to create comprehensive documentation for each LeetCode problem. Follow the exact structure and sections outlined below to maintain consistency across all problem documentation.

---

## Template Structure

### 1. **Header**
```markdown
# [Problem Number]. [Problem Title]
```

### 2. **Problem Statement**
```markdown
## Problem Statement

[Copy the exact problem statement from LeetCode]

[Include any additional context or guarantees mentioned in the problem]
```

### 3. **Examples**
```markdown
## Examples

### Example 1:
```
Input: [input]
Output: [output]
```

### Example 2:
```
Input: [input]
Output: [output]
```

[Add more examples if provided]
```

### 4. **Constraints**
```markdown
## Constraints

- [List all constraints exactly as given]
- [Include data ranges]
- [Include array size limits]
- [Include any guarantees about the result]
```

### 5. **Follow-up (if applicable)**
```markdown
## Follow-up
[Any follow-up questions or optimization challenges]
```

### 6. **Core Requirements** ⭐
```markdown
## Core Requirements

### 1. **Functional Requirements**
- **Input**: [Describe input format and constraints]
- **Output**: [Describe expected output format]
- **Element Range**: [Data type and value ranges]
- **Result Guarantee**: [Any guarantees about the result]

### 2. **Performance Constraints**
- **Time Complexity**: [Required time complexity]
- **Space Complexity**: 
  - **Primary Goal**: [Main space requirement]
  - **Follow-up Goal**: [Optimized space requirement if applicable]

### 3. **Algorithm Restrictions**
- **Forbidden Operations**: [List any operations not allowed]
- **Special Considerations**: [Any special rules or restrictions]
- **Edge Case Handling**: [Must handle specific edge cases]

### 4. **Critical Edge Cases**
- **Case 1**: `[input]` → `[output]` - [explanation]
- **Case 2**: `[input]` → `[output]` - [explanation]
- **Case 3**: `[input]` → `[output]` - [explanation]
- **Case 4**: `[input]` → `[output]` - [explanation]

### 5. **Success Criteria**
- ✅ [Criterion 1]
- ✅ [Criterion 2]
- ✅ [Criterion 3]
- ✅ [Criterion 4]
- ✅ (Bonus) [Optional optimization criterion]

### 6. **Pattern Recognition Requirements**
- **Identify**: This is a **[Pattern Name]** problem
- **Approach**: [Brief description of algorithmic approach]
- **Key Insight**: [The crucial insight needed to solve the problem]
```

### 7. **Pattern Recognition**
```markdown
## Pattern Recognition

This problem follows the **[Pattern Name]** pattern:
- **Pattern Type**: [Category of algorithmic pattern]
- **Core Idea**: [Main concept behind the pattern]
- **Key Insight**: [Critical understanding needed]
```

### 8. **Solution Approach**
```markdown
## Solution Approach

### Algorithm: [Algorithm Name]

1. **Step 1**: [Description of first major step]
2. **Step 2**: [Description of second major step]
3. **Step N**: [Continue for all major steps]

### Visual Walkthrough

For `input = [example input]`:

```
[Step-by-step visual representation of the algorithm]
[Use ASCII art, tables, or clear text formatting]
[Show intermediate states and transformations]
```

[Final Result: [expected output]]
```

### 9. **Implementation**
```markdown
## Implementation

```python
from typing import List

class Solution:
    def [methodName](self, [parameters]) -> [return_type]:
        [Clean, optimized implementation]
        [Include meaningful variable names]
        [Add brief inline comments for complex logic]
        
        return [result]
```

### 10. **Complexity Analysis**
```markdown
## Complexity Analysis

### Time Complexity: O([complexity])
- **Step 1**: O([complexity]) - [explanation]
- **Step 2**: O([complexity]) - [explanation]
- **Total**: O([overall complexity])

### Space Complexity: O([complexity])
- [Variable/structure 1]: O([complexity]) - [explanation]
- [Variable/structure 2]: O([complexity]) - [explanation]
- **Total**: O([overall complexity])
```

### 11. **Edge Cases**
```markdown
## Edge Cases

### 1. [Edge Case Name]
```python
Input: [input]
Output: [output]
```
- [Explanation of why this is challenging]
- [How the algorithm handles it]

### 2. [Edge Case Name]
```python
Input: [input]
Output: [output]
```
- [Explanation]

[Continue for all significant edge cases]
```

### 12. **Alternative Approaches**
```markdown
## Alternative Approaches

### Approach 1: [Approach Name] ([Why it doesn't work/isn't optimal])
```python
# [Brief comment about why this approach is shown]
def [methodName]_[approach_name](self, [parameters]):
    [Implementation]
    [Show why this violates constraints or is suboptimal]
```

### Approach 2: [Another Approach Name]
```python
# [Comment about this approach]
def [methodName]_[approach_name](self, [parameters]):
    [Implementation]
    [Explain trade-offs]
```

[Continue for other notable approaches]
```

### 13. **Optimization Notes**
```markdown
## Optimization Notes

1. **[Optimization Type]**: [Description of optimization and its impact]
2. **[Optimization Type]**: [Description]
3. **[Limitation]**: [Explanation of why certain optimizations aren't possible]
```

### 14. **Common Mistakes**
```markdown
## Common Mistakes

1. **[Mistake Type]**: [Description and why it's wrong]
2. **[Mistake Type]**: [Description and how to avoid it]
3. **[Mistake Type]**: [Description]
4. **[Mistake Type]**: [Description]
```

### 15. **Related Problems**
```markdown
## Related Problems

- **[Problem Number]. [Problem Name]** - [How it's related/similar pattern]
- **[Problem Number]. [Problem Name]** - [Relationship description]
- **[Problem Number]. [Problem Name]** - [Pattern connection]
- **[Problem Number]. [Problem Name]** - [Algorithmic similarity]
```

### 16. **Test Cases**
```markdown
## Test Cases

```python
def test_solution():
    solution = Solution()
    
    # Basic test cases
    assert solution.[methodName]([input1]) == [expected1]
    assert solution.[methodName]([input2]) == [expected2]
    
    # Edge cases
    assert solution.[methodName]([edge_case1]) == [expected1]
    assert solution.[methodName]([edge_case2]) == [expected2]
    assert solution.[methodName]([edge_case3]) == [expected3]
    assert solution.[methodName]([edge_case4]) == [expected4]
    
    print("All test cases passed!")
```

### 17. **Key Takeaways**
```markdown
## Key Takeaways

1. **[Takeaway 1]**: [Explanation]
2. **[Takeaway 2]**: [Explanation]
3. **[Takeaway 3]**: [Explanation]
4. **[Takeaway 4]**: [Explanation]
5. **[Takeaway 5]**: [Explanation]

[Final summary sentence about the problem's significance or learning value]
```

---

## Section Guidelines

### **Core Requirements Section** (Most Important)
- This is the **most critical section** that differentiates this template
- Must be comprehensive and specific
- Should serve as a quick reference for problem constraints
- Include specific examples for edge cases
- Use checkboxes for success criteria

### **Pattern Recognition**
- Identify the specific algorithmic pattern
- Connect to similar problems
- Explain the key insight needed

### **Visual Walkthrough**
- Always include a step-by-step example
- Use clear formatting (tables, ASCII art, or structured text)
- Show intermediate states, not just final result

### **Implementation**
- Provide the optimal solution
- Use clean, readable code
- Include type hints
- Add brief comments for complex logic

### **Alternative Approaches**
- Show why other approaches don't work
- Explain constraint violations
- Demonstrate learning progression

### **Test Cases**
- Include comprehensive test suite
- Cover all edge cases mentioned
- Use assert statements for verification

---

## File Naming Convention

```
[problem-number]-[problem-title-kebab-case].md
```

Examples:
- `238-product-of-array-except-self.md`
- `1-two-sum.md`
- `15-3sum.md`

---

## Usage Instructions

1. Copy this template for each new problem
2. Fill in all sections systematically
3. Pay special attention to the **Core Requirements** section
4. Test all code examples before documenting
5. Ensure consistency with this exact structure
6. Include meaningful examples and edge cases
7. **Update the root README.md file** with the new problem entry

### Updating Root README.md

When adding a new problem, you must update the root [`README.md`](README.md) file:

#### Add Table Entry
Add a new row to the appropriate difficulty table:

```markdown
| [Problem Number] | [Problem Title](path/to/problem/folder/) | [Python](path/to/solution.py) | [📖](path/to/documentation.md) | [Pattern Name] |
```

#### Update Pattern Categories
If introducing a new pattern, add it to the "Pattern Categories" section:

```markdown
### [New Pattern Category]
- **[Problem Number]. [Problem Title]** - [Pattern Description]
```

#### Update Statistics
Update the statistics section:
- Increment total problems count
- Increment appropriate difficulty count
- Maintain 100% documentation coverage

#### Update Last Modified
Update the footer with current date and new problem count:

```markdown
*Last Updated: [Current Date]*  
*Problems Documented: [New Count]*  
*Documentation Coverage: 100%*
```

Example update for adding problem 15. 3Sum:
```markdown
| 15 | [3Sum](medium/15-3sum/) | [Python](medium/15-3sum/15-3sum.py) | [📖](medium/15-3sum/15-3sum.md) | Two Pointers |
```

---

## Quality Checklist

Before finalizing documentation, verify:

- [ ] All sections are present and complete
- [ ] Core Requirements section is comprehensive
- [ ] Code examples are tested and working
- [ ] Edge cases are covered with examples
- [ ] Pattern recognition is accurate
- [ ] Related problems are relevant
- [ ] Test cases cover all scenarios
- [ ] Visual walkthrough is clear and helpful
- [ ] Common mistakes section adds value
- [ ] Key takeaways summarize learning points
- [ ] **Root README.md file has been updated with new problem entry**
- [ ] **Pattern categories section updated if new pattern introduced**
- [ ] **Statistics section reflects new problem count**

---

This template ensures consistent, comprehensive documentation that serves as both a learning resource and a quick reference for LeetCode problem solving.
