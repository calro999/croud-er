import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"

def check_cids(label, cids):
    print(f"\n=== Testing {label} ===")
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
        if res.status_code == 200:
            items = res.json().get("result", {}).get("items", [])
            if items:
                it = items[0]
                title = it.get("title")
                img = it.get("imageURL", {}).get("large")
                acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
                samples = it.get("sampleImageURL", {})
                s_count = len(samples.get("sample_l", {}).get("image", [])) if "sample_l" in samples else 0
                print(f"✅ [{cid}] {title[:35]}... | 女優: {acts} | サンプル画像数: {s_count}")
            else:
                print(f"❌ [{cid}] Not found in API")
        else:
            print(f"❌ [{cid}] HTTP {res.status_code}")

# 1. アナル
check_cids("アナル特化", ["1asex00003", "juny00042", "1kuse00039", "1nhdtb00842", "mdhr00002"])

# 2. 男の娘
check_cids("男の娘特化", ["dass00731", "dass00568", "dass00693", "dass00616", "dass00656"])

# 3. 黒ギャル
check_cids("黒ギャル特化", ["waaa00136", "bony00152", "mird00243", "blk00681", "manx00018"])
