## Output constraints

### Punctuation
Em dashes are excluded from all Krutho outputs: documents, copy, 
specifications, code comments, and commit messages.

If an em dash construction is reached during drafting, resolve it 
before output using the structurally correct alternative:

- Colon: second clause elaborates or defines the first
- Period: clauses are separable statements  
- Comma: relationship is genuinely parenthetical
- Restructure: none of the above applies

The choice is determined by sentence structure. It is not a 
preference decision.

Note: the user may use em dashes in prompts and conversation. 
This constraint applies to Claude's output only.

---

## Session Start Protocol

At the start of every session, before anything else:

1. Check `context/uploads/` for any `.md` files
2. If files exist, read each one
3. Compare content against `context/context.md`
4. Merge any new information into `context/context.md` under the correct sections
5. Move processed files to `context/uploads/processed/`
6. Confirm: "Context updated from [filename]" or "No new uploads found"

Do not duplicate information already present in context.md.
Do not alter the structure of context.md — only append within existing sections
or add new sections at the end if the category does not exist.

## context/context.md Structure

Sections in order:
- Project Overview
- Key Decisions (dated)
- Open Questions
- Technical Specifications
- Constraints
- Next Steps

---