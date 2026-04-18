const API_URL = '/api/analyze';

async function analyzeText() {
    const scriptInput = document.getElementById('script-input');
    const analyzeBtn = document.getElementById('analyze-button');
    const resultsSection = document.getElementById('results-section');
    const resultsContent = document.getElementById('results-content');
    const text = scriptInput.value.trim();

    if (!text) {
        alert('Please paste some text to analyze.');
        return;
    }

    // UI state: Loading
    analyzeBtn.classList.add('loading');
    analyzeBtn.disabled = true;
    resultsSection.classList.add('hidden');

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: text }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Success: Render results
        displayResults(data);
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to analyze text. Please ensure the backend is running.');
    } finally {
        analyzeBtn.classList.remove('loading');
        analyzeBtn.disabled = false;
    }
}

function displayResults(data) {
    const resultsSection = document.getElementById('results-section');
    const resultsContent = document.getElementById('results-content');

    resultsContent.innerHTML = `
        <div class="result-item">
            <span class="result-value">${data.word_count || 0}</span>
            <span class="result-label">Words</span>
        </div>
        <div class="result-item">
            <span class="result-value">${data.character_count || 0}</span>
            <span class="result-label">Characters</span>
        </div>
        <div class="result-item" style="grid-column: 1 / -1; text-align: left;">
            <span class="result-label">Status</span>
            <p style="margin-top: 5px; color: var(--success-color)">${data.message}</p>
        </div>
    `;

    resultsSection.classList.remove('hidden');
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}

function clearResults() {
    document.getElementById('script-input').value = '';
    document.getElementById('results-section').classList.add('hidden');
}
