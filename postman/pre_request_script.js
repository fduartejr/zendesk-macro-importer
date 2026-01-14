const title = pm.iterationData.get("title");
const activeRaw = String(pm.iterationData.get("active") || "").toLowerCase();
const active = ["true","1","yes","y"].includes(activeRaw);
const actions = JSON.parse(pm.iterationData.get("actions_json"));
pm.request.body.raw = JSON.stringify({ macro: { title, active, actions } });
