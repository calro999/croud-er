import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"

cids = ["miab00504", "migd00762", "fstu00030", "savr01215", "h_1293mbg00002"]
url = "https://api.dmm.com/affiliate/v3/ItemList"
for cid in cids:
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "cid": cid,
        "output": "json"
    }
    res = requests.get(url, params=params)
    items = res.json().get("result", {}).get("items", [])
    if items:
        it = items[0]
        title = it.get("title")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        samples = len(it.get("sampleImageURL", {}).get("sample_l", {}).get("image", []))
        print(f"[{cid}] {title[:35]} | 女優: {acts} | サンプル: {samples}")
