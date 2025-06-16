# 📋 CapeControl Development Checklist

## ✅ Backend

- [x] Setup FastAPI app with CORS middleware
- [x] Create `/register` and `/login` routes
- [x] Add password hashing and token creation
- [x] Implement `/me` protected route
- [ ] Move all backend code into `backend/app/` for clarity and maintainability
- [ ] Organize route files under `backend/app/routes/` and include routers modularly in `main.py`
- [ ] Ensure all backend imports use `from app ...` instead of `from backend ...`
- [ ] Use environment variables for sensitive data (e.g., database URLs) in backend
- [ ] Add a `get_db` dependency for database sessions in FastAPI
- [ ] Add role-based access control
- [ ] Add error logging to all routes
- [ ] Add docstrings and comments to all models, schemas, and complex logic
- [ ] Use `from_attributes = True` in Pydantic schema `Config` for ORM mode
- [ ] Move utility scripts to the `scripts/` directory
- [ ] Ensure Docker and Compose files are at the project root and updated for new structure

## ✅ Frontend (React + Tailwind)

- [x] Setup Vite + Tailwind project
- [x] Create `Login` and `Register` forms
- [ ] Hook login form to backend
- [ ] Store token in localStorage
- [ ] Create Dashboard with `/me` fetch
- [ ] Centralize error handling in hooks and API utilities
- [ ] Refactor long functions into smaller, modular pieces
- [ ] Extract reusable logic (like data fetching) into custom hooks with JSDoc comments
- [ ] Use functional components and hooks in React code
- [ ] Use `useMemo` and `useCallback` for performance optimization in React
- [ ] Use PropTypes or TypeScript for type checking in React components
- [ ] Add and configure ESLint with a custom config to enforce:
    - camelCase for variables and functions
    - single quotes for string literals
    - 2-space indentation
- [ ] Add Prettier for consistent code formatting
- [ ] Add an `ignores` property in `eslint.config.js` to exclude `dist/`, `build/`, and config files from linting
- [ ] Remove `.eslintignore` file if present
- [ ] Use BEM naming convention and CSS variables in styles
- [ ] Keep styles modular and avoid global styles
- [ ] Use Flexbox or Grid for layout in CSS
- [ ] Add unit tests for custom hooks and utility functions
- [ ] Use modern JavaScript/TypeScript syntax and best practices throughout the codebase

## ✅ DevOps

- [x] Setup Dockerfile for backend
- [x] Create docker-compose.yml with Postgres
- [ ] Add `.env` file for secrets
- [ ] Setup GitHub Actions for CI

---

### ⏳ In Progress
- Hooking login form to backend
- Testing /me route with JWT

---

**Note:**  
- Always use camelCase for variables and functions.  
- Indent with two spaces.  
- Use single quotes for all string literals.  
- Add comments for functions and any complex logic.  
- Break long functions into smaller, modular pieces.  
- Remove redundant code and use modern JavaScript syntax (e.g., arrow functions, destructuring).  
- Extract reusable logic (like data fetching) into custom hooks.  
- Use functional components and hooks in React.  
- Use PropTypes or TypeScript for type checking.  
- Use BEM naming convention and CSS variables in styles.  
- Keep styles modular and avoid global styles.  
- Use Flexbox or Grid for layout in CSS.  
- Add unit tests for custom hooks and utility functions.  
- Centralize error handling in hooks and API utilities.  
- Use modern JavaScript/TypeScript syntax and best practices throughout the codebase.  