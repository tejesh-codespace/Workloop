/**
 * WorkLoop WhatsApp Business Cloud API interactive reply button helper.
 */
export async function sendDailyJobAlert(toPhone, workerName, role) {
  const url = `https://graph.facebook.com/v21.0/${process.env.WHATSAPP_PHONE_NUMBER_ID}/messages`;
  const payload = {
    messaging_product: "whatsapp",
    to: toPhone,
    type: "interactive",
    interactive: {
      type: "button",
      body: {
        text: `Good Morning ${workerName}! New ${role} jobs are open near you.`,
      },
      action: {
        buttons: [
          { type: "reply", reply: { id: "NEW_JOBS", title: "New job postings" } },
          { type: "reply", reply: { id: "ALL_JOBS", title: "All nearby jobs" } },
        ],
      },
    },
  };
  const res = await fetch(url, {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.WHATSAPP_ACCESS_TOKEN}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return await res.json();
}
