import React from 'react';

/**
 * PRESENTATION VIEWER COMPONENT
 * -----------------------------
 * ❌ NOTE: You cannot embed a Google Drive URL directly in an iframe because 
 * Drive sets 'X-Frame-Options: SAMEORIGIN' to prevent this.
 * 
 * ✅ SOLUTION: 
 * 1. Download the bundled HTML file from Drive.
 * 2. Place it in your React application's 'public/' folder.
 * 3. Use this component to display it.
 */

const PresentationViewer = () => {
    // This path must match where you put the file in your public folder
    const presentationUrl = '/13-01-2026-B1-Tech-Presentation.html';

    return (
        <div style={{ width: '100%', height: '100vh', overflow: 'hidden' }}>
            <iframe
                src={presentationUrl}
                title="B1 Tech Article Presentation"
                width="100%"
                height="100%"
                style={{ border: 'none' }}
                allowFullScreen={true}
                loading="lazy"
            />
        </div>
    );
};

export default PresentationViewer;
