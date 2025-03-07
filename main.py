import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
    #identidade
    name = ''
    #Request
    def start_requests(self):
        #definindo a url para varrer 
        urls = ['']#url do site 
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 
    #response
    def parse(self, response):	
        #aqui é onde você vai colocar o código para extrair as informações da página
        for elemento in response.xpath(''):#campo para selecionar o XPATH do campo que deseja extrair
            yield{
                #campo para oq voce deseja extrair dados menores
            }

        
        try:#tratamento para parar quando não houver mais paginas 
            link_para_proxima_pagina = response.xpath('').get()#metodo inteligente e legal para selecionar mais paginas para extração de dados
            if link_para_proxima_pagina is not None:
                link_para_proxima_pagina_completo = response.urljoin(link_para_proxima_pagina)
                yield scrapy.Request(url=link_para_proxima_pagina_completo, callback=self.parse)
        except:
            print("Chegamos na ultima página")
            