# 📋 CapeControl Development Checklist

## ✅ Backend

- [x] Setup FastAPI app with CORS middleware
- [x] Create `/register` and `/login` routes
- [x] Add password hashing and token creation
- [x] Implement `/me` protected route
- [ ] Add role-based access control
- [ ] Add error logging to all routes

## ✅ Frontend (React + Tailwind)

- [x] Setup Vite + Tailwind project
- [x] Create `Login` and `Register` forms
- [ ] Hook login form to backend
- [ ] Store token in localStorage
- [ ] Create Dashboard with `/me` fetch

## ✅ DevOps

- [x] Setup Dockerfile for backend
- [x] Create docker-compose.yml with Postgres
- [ ] Add `.env` file for secrets
- [ ] Setup GitHub Actions for CI

---

### ⏳ In Progress
- Hooking login form to backend
- Testing /me route with JWT
