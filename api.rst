.. currentmodule:: EasyFN-Endpoints

API Reference
=============

Authentication
-------------------------
Authentication related requests use both https://www.epicgames.com and https://account-public-service-prod.ol.epicgames.com.

Authentication Flow
~~~~~~~~~~~~~~
TODO! For now, I recommend you check out these implementations on how to authenticate:
(https://gist.github.com/Terbau/9a07849fb30c0232af730265c327e27c) [Python Auth Flow by Terbau]_


Account Service
=============
BASE_URL_PROD = "https://account-public-service-prod.ol.epicgames.com/account/";_

BASE_URL_PROD_ALT = "https://account-public-service-prod.ak.epicgames.com/account/";_

BASE_URL_STAGE = "https://account-public-service-stage.ol.epicgames.com/account/"_

	 * grant_type: authorization_code; | fields: code
   
	 * grant_type: client_credentials
   
	 * grant_type: device_auth; | fields: account_id, device_id, secret
   
	 * grant_type: | exchange_code; | fields: exchange_code
   
	 * grant_type: | external_auth; fields: | external_auth_type, | external_auth_token
   
	 * grant_type: otp; fields: otp, challenge
   
	 * grant_type: password; fields: username, password
   
	 * grant_type: refresh_token; fields: refresh_token
   
