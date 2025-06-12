document.getElementById('summarizeButton').addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    chrome.scripting.executeScript({
        target: { tabId: tab.id },
        function: getPageContent,
    }, (results) => {
        const pageContent = results[0].result;
        summarizeContent(pageContent);
    });
});

function getPageContent() {
    return document.body.innerText; // Get the text content