# GitHub Copilot Instructions for JavaScript Projects

## General Code Style Preferences

- **Variable Naming**: Always use `camelCase` for variable and function names.
- **Indentation**: Use **two spaces only** for indentation.
- **Quotes**: Prefer **single quotes** for string literals in JavaScript.
- **Comments**: Add clear and concise comments for functions and complex logic to improve readability.
- **Modularity**: Break down long functions into smaller, more manageable, and modular pieces.
- **Redundancy**: Identify and correct redundant code.
- **Modern Syntax**: Upgrade syntax to be more modern where applicable.
- **Performance**: Suggest performance improvements.

## Refactoring Principles

- Restructure existing code **without changing its functionality** to make it more efficient and easier to understand.
- Break down long functions.
- Extract logic (e.g., data fetching) into custom hooks to centralize and make it reusable.

## Code Review Principles

- Focus on catching bugs, improving code quality, and ensuring consistency.
- Highlight inconsistencies with naming conventions and structures.

## Important Note for Copilot Interaction

- The more specific context you provide (e.g., having related files open, selecting relevant code), the better Copilot's suggestions will be.
- When prompting Copilot, adhere to the "3 S Principle":  
    - **Simple**: Break down complex requests into smaller, manageable steps.
    - **Specific**: Provide clear context using agents like `@workspace` or file variables like `#file` or `#editor`.
    - **Short**: Use concise prompts; formal grammar is not required.

## Automate Style Enforcement

    - Use ESLint with a custom config to enforce camelCase, single quotes, and 2-space indentation.
    - Add Prettier for consistent formatting.

## Document Custom Hooks and Utilities

    -When extracting logic into hooks, add JSDoc comments for usage and expected parameters/returns.

## When writing or refactoring JavaScript code:

    Always use camelCase for variables and functions.
    Indent with two spaces.
    Use single quotes for all string literals.
    Add comments for functions and any complex logic.
    Break long functions into smaller, modular pieces.
    Remove redundant code and use modern JavaScript syntax (e.g., arrow functions, destructuring).
    Extract reusable logic (like data fetching) into custom hooks.
## When writing or refactoring React code:
- Use functional components and hooks.
- Use `useState` and `useEffect` for state management and side effects.
- Use `useContext` for global state management.
- Use `PropTypes` or TypeScript for type checking.
- Use `useMemo` and `useCallback` to optimize performance where necessary.
- Ensure components are modular and reusable.
## When writing or refactoring CSS:
- Use BEM (Block Element Modifier) naming convention for classes.
- Use CSS variables for colors and common styles.
- Keep styles modular and avoid global styles.
- Use Flexbox or Grid for layout.
## When writing or refactoring TypeScript code:
- Use `interface` for defining object shapes.
- Use `type` for defining unions or more complex types.
- Use `enum` for defining a set of named constants.
- Use `unknown` instead of `any` for better type safety.
- Use `as const` for literal types when necessary.
- Use `async/await` for asynchronous code.
- Use `Promise` for handling asynchronous operations.
- Use `never` for functions that never return (e.g., throwing errors).
- Use `readonly` for properties that should not be modified.
- Use `Partial<T>` for functions that accept partial objects.
- Use `Record<K, T>` for objects with specific key-value pairs.
- Use `Pick<T, K>` for creating a new type by picking specific properties from an existing type.
- Use `Omit<T, K>` for creating a new type by omitting specific properties from an existing type.
- Use `ReturnType<T>` for getting the return type of a function.
- Use `Parameters<T>` for getting the parameter types of a function.
- Use `Awaited<T>` for getting the resolved type of a promise.
- Use `NonNullable<T>` for excluding `null` and `undefined` from a type.
- Use `Exclude<T, U>` for excluding specific types from a union type.
- Use `Extract<T, U>` for extracting specific types from a union type.
## When writing or refactoring Node.js code:
- Use `async/await` for asynchronous operations.
- Use `express` for building web applications.
- Use `mongoose` for MongoDB interactions.
- Use `dotenv` for environment variable management.
- Use `cors` for handling cross-origin requests.
- Use `helmet` for securing HTTP headers.
- Use `winston` or `morgan` for logging.
- Use `jest` or `mocha` for testing.
- Use `supertest` for testing HTTP endpoints.
- Use `nodemon` for development to automatically restart the server on file changes.
- Use `pm2` for process management in production.
## When writing or refactoring code in general:
- Use `async/await` for asynchronous operations.
- Use `try/catch` for error handling.
- Use `console.error` for logging errors.
- Use `console.warn` for logging warnings.
- Use `console.info` for logging informational messages.
- Use `console.debug` for logging debug messages.
- Use `console.log` for logging general messages.
- Use `console.table` for logging tabular data.
- Use `console.group` and `console.groupEnd` for grouping related log messages.
- Use `console.time` and `console.timeEnd` for measuring performance.
- Use `console.assert` for assertions in code.
- Use `console.trace` for logging stack traces.
                                                                                                                            # GitHub Copilot Instructions for JavaScript Projects

## When reviewing code:

Check for bugs and code quality issues.
Ensure naming conventions and file structures are consistent.
Highlight any code that doesn’t follow these standards.

## When asking for help or code generation:

Be specific about what you want (e.g., “Refactor this function for modularity” or “Extract data fetching into a custom hook”).
Select or reference the relevant code or file.
Keep your requests simple and focused.
