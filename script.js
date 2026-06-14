const textarea = document.querySelector("#noteInput");
const button = document.querySelector("#generateBtn");
const paragraph = document.querySelector("#infoText");
button.addEventListener("click",async (e) => {
   const text = textarea.value;
 try {
    const req = await fetch("/summary", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
    });
  const data = await req.json();
  paragraph.textContent = data.summary;
  paragraph.classList.remove("hidden");
  } catch (error) {
    console.log("Fetch error:", error);
    paragraph.textContent = error
  }
});