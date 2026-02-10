# Local Server Deployment Skill

Deploy and preview Reveal.js presentations locally with reliable background execution and source preview capabilities.

## Quick Start

### Start Server (Recommended)
This command starts the server in a separate, non-locking window.
```powershell
# From project root
npm run server:bg
```

### Access Presentations
- **Root index:** http://127.0.0.1:8080/
- **Built lesson (dist):** http://127.0.0.1:8080/[lesson-folder]/
- **Source Preview (inputs):** http://127.0.0.1:8080/inputs/[lesson-folder]/published/

## NPM Scripts

| Script | Description |
|--------|-------------|
| `npm run server:bg` | **Recommended.** Start server in a separate, non-locking window. |
| `npm start` | Start server in current terminal (locks terminal). |
| `npm run dev:external` | Allow access from other devices (HOST=0.0.0.0). |
| `npm run build` | Rebuild dist folder. |
| `npm run preview` | Build + start server. |

## Instant Source Preview
You can now preview changes immediately without running a build.
1. Edit `inputs/[Lesson]/presentation.json`
2. Run `generate_presentation.py` (or let `fast_edit.py` do it)
3. Navigate to: `http://127.0.0.1:8080/inputs/[Lesson]/published/index.html`

## External Access (Tablet/Laptop)

1. Find your IP address:
   ```powershell
   ipconfig
   ```
   Look for `IPv4 Address` under your WiFi adapter.

2. Start server with external access:
   ```powershell
   npm run dev:external
   ```

3. Access from other device:
   ```
   http://<your-ip>:8080/
   ```

## Troubleshooting

### Port Already in Use
```powershell
# Find process using port 8080
netstat -ano | findstr :8080
# Kill the process
taskkill /PID <PID> /F
```

### Files Not Updating
- If viewing the **Built** version (`dist`): Run `npm run build` or `fast_edit.py`.
- If viewing the **Source** version (`inputs`): Just refresh the page.
- Hard refresh browser (Ctrl+Shift+R) to clear cache.