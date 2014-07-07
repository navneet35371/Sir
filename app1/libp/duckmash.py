import unirest

response = unirest.get("https://duckduckgo-duckduckgo-zero-click-info.p.mashape.com/?q=allahabad&callback=process_duckduckgo&no_html=1&no_redirect=1&skip_disambig=1&format=json",
headers={
   	"X-Mashape-Authorization": "nEqbg6i8Cxo2xN3wSScbRmnL9h1gCgSb"
}
);
return response.body
