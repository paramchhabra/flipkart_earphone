import requests
from rich import print
import json
import time

def create_session():
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,eu;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'T=TI173652508766200220910369273421766129086286859018626868038963392856; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzgyNTMwODcsImlhdCI6MTczNjUyNTA4NywiaXNzIjoia2V2bGFyIiwianRpIjoiMDk1ZTNiMDQtYmNmNy00ZTk0LTk4YTEtODU1ODI5MTJlZTYxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzM2NTI1MDg3NjYyMDAyMjA5MTAzNjkyNzM0MjE3NjYxMjkwODYyODY4NTkwMTg2MjY4NjgwMzg5NjMzOTI4NTYiLCJrZXZJZCI6IlZJNDBCODZEQ0E1NThBNEQyMkE3MkUwODlGMzUxQzhDNjQiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.r5tsyZ8aTgx0dL1KNO2AU-N01J5blkaLjpBQzajMFbI; K-ACTION=null; ud=9.ZacZCZx_6D0LWOxvVx-1tfR3iHWm0iFRMU1rv91j0HceYs0LsAp_U5CUBwmnBMRcj_RcXFoh5lDg7pHHRS5wSxgZxE38f5pgJWoJrhnZwu38DmVf82Jd91eiNJMbtH_lu_1X3l23p9eLyYekhDErtQ; vh=927; vw=1920; dpr=1; Network-Type=4g; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20099%7CMCMID%7C31554515999645108282681720627781521005%7CMCAAMLH-1737129891%7C12%7CMCAAMB-1737129891%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1736532291s%7CNONE%7CMCAID%7CNONE; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; rt=null; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aaudio-video%25253Aheadset%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Faudio-video%25252Fheadset%25252Fpr%25253Fsid%25253D0pm%2525252Cfcn%252526p%2525255B%2525255D%25253Dfacets.connectivity%252525255B%252525255D%252525%2526ot%253DA; S=d1t12Jj8/ej8EPwwlQz8/Pz8/Od02uMu6P6iY0jFlWKQb/s1QdhaLicv+afAwZ1mLrJVVLmU79wLVtHbklJZiOMZziA==; SN=VI40B86DCA558A4D22A72E089F351C8C64.TOKA35E8D0FF6044AEA8C5C5DB66E6091A2.1736525696746.LO; vd=VI40B86DCA558A4D22A72E089F351C8C64-1736525095693-1.1736525696.1736525095.153671455',
        'Origin': 'https://www.flipkart.com',
        'Referer': 'https://www.flipkart.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'X-User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    proxy = "http://USER329062-zone-custom:acb5f2@global.711proxy.com:10000"

    # Set up the proxies dictionary
    proxies = {
        "http": proxy,
        "https": proxy
    }

    session = requests.Session()
    session.headers.update(headers)
    session.proxies.update(proxies)

    return session

cookies = {
    'T': 'TI173652508766200220910369273421766129086286859018626868038963392856',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzgyNTMwODcsImlhdCI6MTczNjUyNTA4NywiaXNzIjoia2V2bGFyIiwianRpIjoiMDk1ZTNiMDQtYmNmNy00ZTk0LTk4YTEtODU1ODI5MTJlZTYxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzM2NTI1MDg3NjYyMDAyMjA5MTAzNjkyNzM0MjE3NjYxMjkwODYyODY4NTkwMTg2MjY4NjgwMzg5NjMzOTI4NTYiLCJrZXZJZCI6IlZJNDBCODZEQ0E1NThBNEQyMkE3MkUwODlGMzUxQzhDNjQiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.r5tsyZ8aTgx0dL1KNO2AU-N01J5blkaLjpBQzajMFbI',
    'K-ACTION': 'null',
    'ud': '9.ZacZCZx_6D0LWOxvVx-1tfR3iHWm0iFRMU1rv91j0HceYs0LsAp_U5CUBwmnBMRcj_RcXFoh5lDg7pHHRS5wSxgZxE38f5pgJWoJrhnZwu38DmVf82Jd91eiNJMbtH_lu_1X3l23p9eLyYekhDErtQ',
    'vh': '927',
    'vw': '1920',
    'dpr': '1',
    'Network-Type': '4g',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C20099%7CMCMID%7C31554515999645108282681720627781521005%7CMCAAMLH-1737129891%7C12%7CMCAAMB-1737129891%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1736532291s%7CNONE%7CMCAID%7CNONE',
    'gpv_pn': 'HomePage',
    'gpv_pn_t': 'FLIPKART%3AHomePage',
    'rt': 'null',
    's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aaudio-video%25253Aheadset%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Faudio-video%25252Fheadset%25252Fpr%25253Fsid%25253D0pm%2525252Cfcn%252526p%2525255B%2525255D%25253Dfacets.connectivity%252525255B%252525255D%252525%2526ot%253DA',
    'S': 'd1t12Jj8/ej8EPwwlQz8/Pz8/Od02uMu6P6iY0jFlWKQb/s1QdhaLicv+afAwZ1mLrJVVLmU79wLVtHbklJZiOMZziA==',
    'SN': 'VI40B86DCA558A4D22A72E089F351C8C64.TOKA35E8D0FF6044AEA8C5C5DB66E6091A2.1736525696746.LO',
    'vd': 'VI40B86DCA558A4D22A72E089F351C8C64-1736525095693-1.1736525696.1736525095.153671455',
    }


def write_data_in_file(url, session, pagenum):
    json_data = {
        'pageUri': '/audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=86&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0gyV1dUWUFFWjhSRDQiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&page=1',
        'pageContext': {
            'fetchSeoData': True,
            'paginatedFetch': True,
            'pageNumber': pagenum,
            'paginationContextMap': {
                'federator': {
                    'pageNumber': pagenum,
                    'AUGMENTATION_CARD': 0,
                    'CATEGORY_TREE': 0,
                    'SERVICEABILITY_CARD': 0,
                    'ADS': 20,
                    'MERCH_CARD': 0,
                    'FILTER_SORT_OPTIONS': 1,
                    'CCM_CONTENT_CARD': 0,
                    'relatedProductsCount': 0,
                    'PRODUCT': 60,
                    'SHOPPING_PREFERENCE': 0,
                    'previousContentTypeServed': 'SEARCH_FEEDBACK_CARD:0',
                    'EMPTY_SEARCH': 1,
                    'widgetOffset': 51,
                    'FILTER_FOOTER': 0,
                    'widgetStart': 50,
                    'store.path': '0pm/fcn',
                    'COMPARE_OPTIONS': 0,
                    'droppedContents': {
                        'skippedProductsPerPage': {
                            '2': [
                                {
                                    'listingId': 'LSTACCGS2VSYQFQ4HTZOQJ1UU',
                                    'skippedReason': 'DEDUPE',
                                },
                                {
                                    'listingId': 'LSTACCG92R6QZWS9SYHR9KG4B',
                                    'skippedReason': 'DEDUPE',
                                },
                                {
                                    'listingId': 'LSTACCH3GFF7ATCGCGHKLHYMO',
                                    'skippedReason': 'DEDUPE',
                                },
                                {
                                    'listingId': 'LSTACCGRZSFXMYJVRZYQUDECT',
                                    'skippedReason': 'DEDUPE',
                                },
                            ],
                        },
                    },
                    'INLINE_FILTER': 0,
                    'SHOP_PRODUCT_CARD': 0,
                    'FILTER_VALUES': 0,
                    'BUTTON_LIST': 0,
                    'productTypeClusterStart': 81,
                    'cursor': '{"paginationCursor":{"cursorType":"djCursor","parentRequestId":"40a1d7f5-d5e1-4837-bbdc-c0bc51fc6c85","cacheKey":null,"offset":0,"hasMoreContent":true,"foldId":1,"foldSize":0,"servedFoldNumber":0,"servedWidgetCount":1,"rankedQueueSize":0,"paginatedContentProviders":null,"lastFold":false,"contentProvidersCursorMap":{"PCA":{"paginationCursor":{"cursorType":"contentProviderCursor","parentRequestId":"40a1d7f5-d5e1-4837-bbdc-c0bc51fc6c85","cacheKey":null,"offset":0,"hasMoreContent":true},"collectionMetaInfoList":[]}},"paginationType":null,"cachedSlotIds":null},"collectionMetaInfoList":[]}',
                    'FILTER_NAVIGATION': 1,
                    'productsOffset': 64,
                    'LAYOUT_OPTIONS': 0,
                    'FILTER_TAB': 0,
                    'INLINE_GUIDE': 0,
                    'MESSAGING_CARD': 0,
                    'SERVICEABILITY_FILTER': 0,
                    'ANNOUNCEMENTS_NAVIGATION': 0,
                    'INLINE_VISUAL_CARD': 0,
                    'feedbackMap': {
                        'SEARCH_FEEDBACK_CARD': [
                            '1',
                        ],
                    },
                    'slot_list_ADS': [
                        41,
                        42,
                        45,
                        47,
                        48,
                        51,
                        52,
                        55,
                        57,
                        58,
                        61,
                        62,
                        65,
                        67,
                        68,
                        71,
                        72,
                        75,
                        77,
                        78,
                    ],
                    'PAGINATION_BAR': 1,
                    'CATEGORY_VALUES': 0,
                    'priceSortSlots': [],
                    'SHOP_CARD': 0,
                    'topAds': 0,
                    'recentlyShownAds': [
                        {
                            'listingId': 'LSTACCGTBG7NSGNKWY4CQRUSZ',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH2WWTZUWTRNHPZ7SX0C',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH6R7PZZYK3ZZG1IJYX6',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGRZSFXMYJVRZYQUDECT',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGSZCDZSXEHWW7EIAG17',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGPW7JKY6HF3A65CG5KB',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH3GFF7ATCGCGHKLHYMO',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGQQ2TQGWRGRM4XKHJFU',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH4V9R3JHCYNET8PIJNB',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH3GFFRZ4FJZKM6Z47T9',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGQQ2TFYGHWBYHV66FXJ',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH6R7PYQXCJF8XHT12NM',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGRNFMDTYGWMW9RGRKAD',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGS2VSYQFQ4HTZ3WCF30',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCG9J7F2NMUB5H6PEDEKB',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCH238YMBHRNHHELZWUN0',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGXYWD3FGKCHYGNJDZSN',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCG5BDHUHJCZ4CGYZPEN9',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCGQQ2T77EFW8HQXUHKMI',
                            'shownExplanation': 'SHOWN',
                        },
                        {
                            'listingId': 'LSTACCG92R6QZWS9SYHR9KG4B',
                            'shownExplanation': 'SHOWN',
                        },
                    ],
                    'FILTER_SORT_BOTTOM': 0,
                    'CLEAR_FILTERS': 0,
                    'TOP_FILTER': 0,
                    'OFFER_HEADER_CARD': 0,
                    'PLA_GROUP_CARD': 0,
                    'layout': 'grid',
                    'productsEnd': 0,
                    'MULTI_CONTENT_CARD': 0,
                    'SEARCH_FEEDBACK_CARD': 1,
                },
            },
        },
        'requestContext': {
            'type': 'BROWSE_PAGE',
            'ssid': '8dq6rnf6400000001736525697358',
            'sqid': 'xrjvnaszds0000001736525710822',
        },
    }
        # response = requests.post('https://1.rome.api.flipkart.com/api/4/page/fetch', cookies=cookies, headers=headers, json=json_data, verify=False)
    response = session.post(url, cookies=cookies, json=json_data, verify=False)
    with open("file.json", "w") as f:
        json.dump(response.json(), f)
        f.close()
    
def main():
    session = create_session()
    url = "https://1.rome.api.flipkart.com/api/4/page/fetch"


    with open("output.txt","a") as f:
        for k in range(1,30):
            write_data_in_file(url, session, k)
            with open("file.json", "r") as g:
                json_obj = json.load(g)
                g.close()

            if "pageData" not in json_obj["RESPONSE"]:
                break


            for i in json_obj["RESPONSE"]["slots"]:
                
                if i["slotType"]!="WIDGET" or "FILTER_SORT_OPTIONS" in str(i["elementId"]):
                    continue
                else:
                    if "PRODUCT_SUMMARY" not in str(i["elementId"]):
                        break
                    else:
                        for j in i["widget"]["data"]["products"]:
                            item = {}
                            j = j["productInfo"]["value"]
                            if "pricing" not in j:
                                continue
                            item["Name"] = j["titles"]["title"]
                            item["Price"] = j["pricing"]["finalPrice"]["value"]
                            item["ID"] = j["id"]
                            item["listingId"] = j["listingId"]
                            f.write(json.dumps(item))
                            f.write("\n")
    
    
        print("Data Written")
        f.close()


    # print(len(itemlist))

if "__main__":
    main()

# print(json_obj["RESPONSE"]["slots"][2]["widget"]["data"]["products"][0]["adInfo"]["productId"])
# print(response.json())
# 
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageUri":"/audio-video/headset/pr?sid=0pm%2Cfcn&p%5B%5D=facets.connectivity%255B%255D%3DBluetooth&sort=popularity&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D599&p%5B%5D=facets.price_range.to%3DMax&p%5B%5D=facets.headphone_type%255B%255D%3DTrue%2BWireless&param=86&hpid=WqCPtE2MbDEYEbYbttXC1qp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJHcmFiIE5vdyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkFDQ0gyV1dUWUFFWjhSRDQiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJCZXN0IFRydWV3aXJlbGVzcyBIZWFkcGhvbmVzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&page=1","pageContext":{"fetchSeoData":true,"paginatedFetch":true,"pageNumber":1,"paginationContextMap":{"federator":{"pageNumber":2,"AUGMENTATION_CARD":0,"CATEGORY_TREE":0,"SERVICEABILITY_CARD":0,"ADS":20,"MERCH_CARD":0,"FILTER_SORT_OPTIONS":1,"CCM_CONTENT_CARD":0,"relatedProductsCount":0,"PRODUCT":60,"SHOPPING_PREFERENCE":0,"previousContentTypeServed":"SEARCH_FEEDBACK_CARD:0","EMPTY_SEARCH":1,"widgetOffset":51,"FILTER_FOOTER":0,"widgetStart":50,"store.path":"0pm/fcn","COMPARE_OPTIONS":0,"droppedContents":{"skippedProductsPerPage":{"2":[{"listingId":"LSTACCGS2VSYQFQ4HTZOQJ1UU","skippedReason":"DEDUPE"},{"listingId":"LSTACCG92R6QZWS9SYHR9KG4B","skippedReason":"DEDUPE"},{"listingId":"LSTACCH3GFF7ATCGCGHKLHYMO","skippedReason":"DEDUPE"},{"listingId":"LSTACCGRZSFXMYJVRZYQUDECT","skippedReason":"DEDUPE"}]}},"INLINE_FILTER":0,"SHOP_PRODUCT_CARD":0,"FILTER_VALUES":0,"BUTTON_LIST":0,"productTypeClusterStart":81,"cursor":"{\\"paginationCursor\\":{\\"cursorType\\":\\"djCursor\\",\\"parentRequestId\\":\\"40a1d7f5-d5e1-4837-bbdc-c0bc51fc6c85\\",\\"cacheKey\\":null,\\"offset\\":0,\\"hasMoreContent\\":true,\\"foldId\\":1,\\"foldSize\\":0,\\"servedFoldNumber\\":0,\\"servedWidgetCount\\":1,\\"rankedQueueSize\\":0,\\"paginatedContentProviders\\":null,\\"lastFold\\":false,\\"contentProvidersCursorMap\\":{\\"PCA\\":{\\"paginationCursor\\":{\\"cursorType\\":\\"contentProviderCursor\\",\\"parentRequestId\\":\\"40a1d7f5-d5e1-4837-bbdc-c0bc51fc6c85\\",\\"cacheKey\\":null,\\"offset\\":0,\\"hasMoreContent\\":true},\\"collectionMetaInfoList\\":[]}},\\"paginationType\\":null,\\"cachedSlotIds\\":null},\\"collectionMetaInfoList\\":[]}","FILTER_NAVIGATION":1,"productsOffset":64,"LAYOUT_OPTIONS":0,"FILTER_TAB":0,"INLINE_GUIDE":0,"MESSAGING_CARD":0,"SERVICEABILITY_FILTER":0,"ANNOUNCEMENTS_NAVIGATION":0,"INLINE_VISUAL_CARD":0,"feedbackMap":{"SEARCH_FEEDBACK_CARD":["1"]},"slot_list_ADS":[41,42,45,47,48,51,52,55,57,58,61,62,65,67,68,71,72,75,77,78],"PAGINATION_BAR":1,"CATEGORY_VALUES":0,"priceSortSlots":[],"SHOP_CARD":0,"topAds":0,"recentlyShownAds":[{"listingId":"LSTACCGTBG7NSGNKWY4CQRUSZ","shownExplanation":"SHOWN"},{"listingId":"LSTACCH2WWTZUWTRNHPZ7SX0C","shownExplanation":"SHOWN"},{"listingId":"LSTACCH6R7PZZYK3ZZG1IJYX6","shownExplanation":"SHOWN"},{"listingId":"LSTACCGRZSFXMYJVRZYQUDECT","shownExplanation":"SHOWN"},{"listingId":"LSTACCGSZCDZSXEHWW7EIAG17","shownExplanation":"SHOWN"},{"listingId":"LSTACCGPW7JKY6HF3A65CG5KB","shownExplanation":"SHOWN"},{"listingId":"LSTACCH3GFF7ATCGCGHKLHYMO","shownExplanation":"SHOWN"},{"listingId":"LSTACCGQQ2TQGWRGRM4XKHJFU","shownExplanation":"SHOWN"},{"listingId":"LSTACCH4V9R3JHCYNET8PIJNB","shownExplanation":"SHOWN"},{"listingId":"LSTACCH3GFFRZ4FJZKM6Z47T9","shownExplanation":"SHOWN"},{"listingId":"LSTACCGQQ2TFYGHWBYHV66FXJ","shownExplanation":"SHOWN"},{"listingId":"LSTACCH6R7PYQXCJF8XHT12NM","shownExplanation":"SHOWN"},{"listingId":"LSTACCGRNFMDTYGWMW9RGRKAD","shownExplanation":"SHOWN"},{"listingId":"LSTACCGS2VSYQFQ4HTZ3WCF30","shownExplanation":"SHOWN"},{"listingId":"LSTACCG9J7F2NMUB5H6PEDEKB","shownExplanation":"SHOWN"},{"listingId":"LSTACCH238YMBHRNHHELZWUN0","shownExplanation":"SHOWN"},{"listingId":"LSTACCGXYWD3FGKCHYGNJDZSN","shownExplanation":"SHOWN"},{"listingId":"LSTACCG5BDHUHJCZ4CGYZPEN9","shownExplanation":"SHOWN"},{"listingId":"LSTACCGQQ2T77EFW8HQXUHKMI","shownExplanation":"SHOWN"},{"listingId":"LSTACCG92R6QZWS9SYHR9KG4B","shownExplanation":"SHOWN"}],"FILTER_SORT_BOTTOM":0,"CLEAR_FILTERS":0,"TOP_FILTER":0,"OFFER_HEADER_CARD":0,"PLA_GROUP_CARD":0,"layout":"grid","productsEnd":0,"MULTI_CONTENT_CARD":0,"SEARCH_FEEDBACK_CARD":1}}},"requestContext":{"type":"BROWSE_PAGE","ssid":"8dq6rnf6400000001736525697358","sqid":"xrjvnaszds0000001736525710822"}}'
#response = requests.post('https://1.rome.api.flipkart.com/api/4/page/fetch', cookies=cookies, headers=headers, data=data)