import requests

class SMSUtils:

    @staticmethod
    def send(numbers: str, variables_values: str) -> bool:
        try:
            # The API endpoint URL
            url = "https://www.fast2sms.com/dev/bulkV2"

            # Payload and headers for the request
            payload = f"variables_values={variables_values}&route=otp&numbers={numbers}"
            headers = {
                'authorization': "YOUR_API_KEY",
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache",
            }

            # Send the POST request
            response = requests.post(url, data=payload, headers=headers)

            # Check if the request was successful
            if response.ok:
                response_data = response.json()
                # Check if the API returned a successful response
                return response_data.get('return', False)
            else:
                return False
        except Exception as e:
            # If an exception occurs, return False
            return False

# Usage example
# sms = SMSUtils()
# success = sms.send("9999999999,8888888888,7777777777", "5599")
# print(f"Message sent successfully: {success}")
