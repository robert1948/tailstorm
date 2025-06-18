export async function getCurrentUser() {
  const token = localStorage.getItem('token');

  if (!token) {
    throw new Error('No token found');
  }

  const res = await fetch('http://127.0.0.1:8000/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!res.ok) {
    const data = await res.json();
    throw new Error(data.detail || 'Failed to fetch user');
  }

  return res.json();
}
