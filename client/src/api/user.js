// client/src/api/user.js
export async function getCurrentUser() {
  const token = localStorage.getItem('token');
  const res = await fetch('http://localhost:8000/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    throw new Error('Unauthorized');
  }

  return await res.json();
}
