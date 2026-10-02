import requests

API_ID = "4Lx0ftRf17Uuad6Ud7Gb"
API_AFFILIATE_ID = "onchan555-999"

def search_popular(keyword, hits=15):
    url = "https://api.dmm.com/affiliate/v3/ItemList"
    params = {
        "api_id": API_ID,
        "affiliate_id": API_AFFILIATE_ID,
        "site": "FANZA",
        "service": "digital",
        "floor": "videoa",
        "keyword": keyword,
        "sort": "rank",
        "hits": hits,
        "output": "json"
    }
    res = requests.get(url, params=params)
    items = res.json().get("result", {}).get("items", [])
    print(f"\n=== KEYWORD: {keyword} (SORT: rank) ===")
    for it in items:
        cid = it.get("content_id")
        title = it.get("title")
        rev = it.get("review") or {}
        r_rate = rev.get("rate")
        r_cnt = rev.get("count")
        acts = [a.get("name") for a in it.get("iteminfo", {}).get("actress", [])]
        print(f"[{cid}] (★{r_rate}, {r_cnt}件) {title} | {acts}")

search_popular("アナル解禁")
search_popular("男の娘 柊かな")
search_popular("黒ギャル 中出し")
