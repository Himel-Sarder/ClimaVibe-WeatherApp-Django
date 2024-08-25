# ClimaVibe-WeatherApp-Django
![image](https://github.com/user-attachments/assets/d4192b17-329e-4e5a-8b54-8ac1f830bbfa)

![image](https://github.com/user-attachments/assets/1beb72f7-bc82-4f52-ac8a-3a0748565cdc)

# ClimaVibe

**ClimaVibe** is a Django-based weather application that provides real-time weather information for predefined cities as well as any city entered by the user. The app uses the OpenWeather API to fetch weather data such as temperature, weather description, and corresponding weather icons.

![ClimaVibe Screenshot](screenshot.png)

## Features

- **Real-time Weather Data**: Fetches current weather information for any city using the OpenWeather API.
- **Predefined Cities**: Displays weather data for predefined cities on the homepage.
- **User Input**: Allows users to search for the weather in any city.
- **Responsive Design**: The UI is styled using Tailwind CSS for a modern and responsive user experience.
- **Dynamic Background**: The background of the app adapts to the current weather condition.

## Technologies Used

- **Django**: Backend framework for handling views, models, and routing.
- **Python**: Programming language used for logic implementation.
- **OpenWeather API**: API service to fetch weather data.
- **Tailwind CSS**: Utility-first CSS framework used for styling.
- **HTML/CSS**: For structuring and designing the user interface.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ClimaVibe.git
   cd ClimaVibe
   ```

2. **Install Dependencies**:
   Ensure you have Python and Django installed. You can install the required packages using `pip`:
   ```bash
   pip install django requests
   ```

3. **Set Up the OpenWeather API Key**:
   - Create a `.env` file in the root directory.
   - Add your OpenWeather API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```
   - If using Django environment settings, you might need to configure the settings to read this key.

4. **Migrate Database**:
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser** (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open your web browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Admin Panel

The admin panel allows you to manage predefined cities for which the weather data is displayed on the homepage.

- **Access the Admin Panel**:
  ```
  http://127.0.0.1:8000/admin/
  ```
  Use the superuser credentials created during setup.

- **Add/Remove Predefined Cities**:
  - Go to the `Predefined Cities` section in the admin panel.
  - Add or remove cities as needed. The app will automatically fetch and display the weather data for these cities on the homepage.

## Customization

- **Adding More Predefined Cities**:
  - You can add more cities in the admin panel as mentioned above, or modify the `predefined_cities` list in the `index` view.

- **Styling**:
  - The app uses Tailwind CSS for styling. You can customize the look and feel by modifying the `index.html` and the custom styles in the `style` tag.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
