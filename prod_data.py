import requests
import json

def get_response(id1, id2):
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
        'rt': 'null',
        's_sq': 'flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aaudio-video%25253Aheadset%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Faudio-video%25252Fheadset%25252Fpr%25253Fsid%25253D0pm%2525252Cfcn%252526p%2525255B%2525255D%25253Dfacets.connectivity%252525255B%252525255D%252525%2526ot%253DA',
        'S': 'd1t12Pyg/P1M/cT8/Tj8/OD8/P9J5JDz8oMGv4z8CdreQcBurUpeoAuvfZ+lPON0CaKMNMxw1d2Yj9wgUT8u8dpNDGg==',
        'vd': 'VI40B86DCA558A4D22A72E089F351C8C64-1736525095693-2.1736530312.1736528316.153442049',
        'SN': 'VI40B86DCA558A4D22A72E089F351C8C64.TOKC7E46FD31B7D4A4ABFBAB22D17C8E33C.1736530313886.LO',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,eu;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'T=TI173652508766200220910369273421766129086286859018626868038963392856; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImQ2Yjk5NDViLWZmYTEtNGQ5ZC1iZDQyLTFkN2RmZTU4ZGNmYSJ9.eyJleHAiOjE3MzgyNTMwODcsImlhdCI6MTczNjUyNTA4NywiaXNzIjoia2V2bGFyIiwianRpIjoiMDk1ZTNiMDQtYmNmNy00ZTk0LTk4YTEtODU1ODI5MTJlZTYxIiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzM2NTI1MDg3NjYyMDAyMjA5MTAzNjkyNzM0MjE3NjYxMjkwODYyODY4NTkwMTg2MjY4NjgwMzg5NjMzOTI4NTYiLCJrZXZJZCI6IlZJNDBCODZEQ0E1NThBNEQyMkE3MkUwODlGMzUxQzhDNjQiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.r5tsyZ8aTgx0dL1KNO2AU-N01J5blkaLjpBQzajMFbI; K-ACTION=null; ud=9.ZacZCZx_6D0LWOxvVx-1tfR3iHWm0iFRMU1rv91j0HceYs0LsAp_U5CUBwmnBMRcj_RcXFoh5lDg7pHHRS5wSxgZxE38f5pgJWoJrhnZwu38DmVf82Jd91eiNJMbtH_lu_1X3l23p9eLyYekhDErtQ; vh=927; vw=1920; dpr=1; Network-Type=4g; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C20099%7CMCMID%7C31554515999645108282681720627781521005%7CMCAAMLH-1737129891%7C12%7CMCAAMB-1737129891%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1736532291s%7CNONE%7CMCAID%7CNONE; rt=null; s_sq=flipkart-prd%3D%2526pid%253Dwww.flipkart.com%25253Aaudio-video%25253Aheadset%25253Apr%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.flipkart.com%25252Faudio-video%25252Fheadset%25252Fpr%25253Fsid%25253D0pm%2525252Cfcn%252526p%2525255B%2525255D%25253Dfacets.connectivity%252525255B%252525255D%252525%2526ot%253DA; S=d1t12Pyg/P1M/cT8/Tj8/OD8/P9J5JDz8oMGv4z8CdreQcBurUpeoAuvfZ+lPON0CaKMNMxw1d2Yj9wgUT8u8dpNDGg==; vd=VI40B86DCA558A4D22A72E089F351C8C64-1736525095693-2.1736530312.1736528316.153442049; SN=VI40B86DCA558A4D22A72E089F351C8C64.TOKC7E46FD31B7D4A4ABFBAB22D17C8E33C.1736530313886.LO',
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

    json_data = {
        'pidLidMap': {
            id1:id2,
            # 'ACCGQQ2TFVCUPJHG': 'LSTACCGQQ2TFVCUPJHGGDMWJC',
        },
        'pincode': '',
        'snippetContext': {
            'facetMap': {
                'facets.rating[]': [
                    '3★ & above',
                    '4★ & above',
                ],
                'facets.price_range.from': [
                    '599',
                ],
                'facets.price_range.to': [
                    'Max',
                ],
                'facets.connectivity[]': [
                    'Bluetooth',
                ],
                'facets.headphone_type[]': [
                    'True Wireless',
                ],
            },
            'layout': 'grid',
            'query': None,
            'queryType': None,
            'storePath': '0pm/fcn',
            'viewType': 'GRID_DEFAULT',
        },
    }

    response = requests.post('https://1.rome.api.flipkart.com/api/4/product/swatch', cookies=cookies, headers=headers, json=json_data, verify=False)

    return response.json()



def get_product_data(json_data, pid):
    data = {}
    json_data = json_data["RESPONSE"]["productSwatchDetails"][pid]["products"][pid]
    data["Price"] = json_data["pricing"]["finalPrice"]["value"]
    data["Name"] = json_data["titles"]["title"]
    return data


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pidLidMap":{"ACCGQQ2TFVCUPJHG":"LSTACCGQQ2TFVCUPJHGGDMWJC"},"pincode":"","snippetContext":{"facetMap":{"facets.rating[]":["3★ & above","4★ & above"],"facets.price_range.from":["599"],"facets.price_range.to":["Max"],"facets.connectivity[]":["Bluetooth"],"facets.headphone_type[]":["True Wireless"]},"layout":"grid","query":null,"queryType":null,"storePath":"0pm/fcn","viewType":"GRID_DEFAULT"}}'.encode()
#response = requests.post('https://1.rome.api.flipkart.com/api/4/product/swatch', cookies=cookies, headers=headers, data=data)