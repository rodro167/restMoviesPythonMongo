# Use the official Python image as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port your application will run on (4000 in your case)
EXPOSE 4000

# Command to run your application
CMD ["python", "mongoRestMovies.py"]
