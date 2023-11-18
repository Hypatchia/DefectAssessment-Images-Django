## Project Overview

<h3 align="center" style=" line-height: 1.5;">The project is a Scalable Django Web App built for Computer Vision-Based Defect Assessment of Images of Pump Impellers.<br>
It provides an effective real time inference solution for assessing product defects.
<br>
The full working django app can be accessed at <a >impellerdefectasssessment.azurewebsites.net</a></h3>

### How it works:

* Images of products will be uploaded by users, and whether the product is defective or defect-free will be predicted by the system.

* The source code and resources for the web application, including the deep learning model used for prediction, are contained in this repository.

### Built with:

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Latest-blue?style=flat&logo=tensorflow)](https://www.tensorflow.org/)
[![Azure](https://img.shields.io/badge/Azure-Latest-blue?style=flat&logo=microsoft-azure)](https://azure.microsoft.com/)
[![Django](https://img.shields.io/badge/Django-Latest-blue?style=flat&logo=django)](https://www.djangoproject.com/)

### Project Steps
- Process and Analyse Images of Submersible Pump Impellers.
- Train, Evaluate and optimize a Convolutional Neural Network in Keras-Tensorflow for Binary Classification.
- Save the best model based on accuracy, recall, precision and AUC ROC Curves.
- Build a Django Backend for real time integration of the AI Based Solution & Designed the FrontEnd
- Deployed the Web App to Azure Web App Services.


### Deployment

* The final web application was deployed on Azure App Services, ensuring scalability and reliability. 
* Azure Blob Containers are used for storing deep learning models and product images for seamless integration with the web application.


* Screenshot for the App:
  <img src="webpage.jpeg" alt="Model Architecture" style="height:0%; width:100%;">


### Setup to run 

* Clone Repository
* Navigate to directory
* Run in terminal
* Create Virtual Environemeent & Activate it
* Install requirements
~~~
pip install requirements.txt
~~~
* Run App
~~~
python manage.py runserver
~~~


## Contact:
Feel free to reach out to me on LinkedIn or through email & don't forget to visit my portfolio.
 
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect%20with%20Me-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/samiabelhaddad/)
  [![Email](https://img.shields.io/badge/Email-Contact%20Me-brightgreen?style=flgat&logo=gmail)](mailto:samiamagbelhaddad@gmail.com)
  [![Portfolio](https://img.shields.io/badge/Portfolio-Visit%20My%20Portfolio-white?style=flat&logo=website)](https://samiabelhaddad.me/)
