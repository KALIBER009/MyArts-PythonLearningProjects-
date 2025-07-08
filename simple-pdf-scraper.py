import requests
import os 
from bs4 import BeautifulSoup
file_downloads = os.makedirs("pdf_files", exist_ok=True)
def download_pdfs():
    the_Url = input('please enter the url: ')
    get_request = requests.get(the_Url)
    try:
            get_request = requests.get(the_Url)
            if get_request.status_code == 200:
                    soup = BeautifulSoup(get_request.content, "html5lib")
                    links = soup.find_all("a")
                    pdfUrl = []
                    for row in links:
                        href = row.get("href")
                        if href is not None and ".pdf" in href:
                            pdfUrl.append(href)
                    if  not pdfUrl:
                                raise ValueError ("error not found")
                    for link in pdfUrl:
                        asking_request = requests.get(link)
                        if asking_request.status_code == 200:
                                book_name =  link.split("/")[-1]
                                path = "pdf_files/" + book_name
                                with open(path, "wb") as f:
                                    f.write(asking_request.content)
                                    print(f"Downloaded: {book_name}")
    except Exception as e:
          print("An error occuerd: ", e)
           
                
            

                          
                   


                
        
        


            






        


            







