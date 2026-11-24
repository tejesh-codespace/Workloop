/**
 * WorkLoop multilingual voice helper (ElevenLabs).
 */
export async function synthesizeVoice(text, voiceId = process.env.ELEVENLABS_VOICE_ID) {
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: "POST",
    headers: { "xi-api-key": process.env.ELEVENLABS_API_KEY, "Content-Type": "application/json" },
    body: JSON.stringify({ text, model_id: "eleven_multilingual_v2" }),
  });
  if (!res.ok) throw new Error(`Voice API error ${res.status}`);
  return await res.arrayBuffer();
}
