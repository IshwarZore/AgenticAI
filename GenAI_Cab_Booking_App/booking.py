from datetime import datetime
from typing import Dict, Optional, Tuple
from uuid import uuid4


class CabBookingService:
    def __init__(self):
        # Store bookings: booking_id -> booking_details
        self.bookings: Dict[str, dict] = {}
        # Store drivers: driver_id -> driver_details
        self.drivers: Dict[str, dict] = {
            "driver101": {"name": "Peter Pandey", "phone": "555-0101", "car": "Toyota Camry"},
            "driver102": {"name": "Bruce Hariyali", "phone": "555-0102", "car": "Honda Accord"},
            "driver103": {"name": "Tony Thakkar", "phone": "555-0103", "car": "Ford Focus"},
            "driver104": {"name": "Steve Sharma", "phone": "555-0104", "car": "Chevrolet Malibu"},
            "driver105": {"name": "Natasha Nanda", "phone": "555-0105", "car": "Nissan Altima"},
        }
        # Track driver availability: driver_id -> is_available
        self.driver_availability: Dict[str, bool] = {
            "driver101": True,
            "driver102": True,
            "driver103": True,
            "driver104": True,
            "driver105": True,
        }

    def book_cab(self, pickup_location: str, dropoff_location: str) -> Tuple[str, str]:
        """
        Book a cab from pickup to dropoff location.
        Returns: (booking_id, driver_id)
        Raises: ValueError if no drivers available or invalid locations
        """
        if not pickup_location or not dropoff_location:
            raise ValueError("Pickup and dropoff locations must be provided")

        # Find available driver
        available_driver = None
        for driver_id, is_available in self.driver_availability.items():
            if is_available:
                available_driver = driver_id
                break

        if not available_driver:
            raise ValueError("No drivers available at the moment")

        # Create booking
        booking_id = str(uuid4())
        booking_details = {
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "driver_id": available_driver,
            "status": "booked",
            "booking_time": datetime.now()
        }

        # Store booking and update driver availability
        self.bookings[booking_id] = booking_details
        self.driver_availability[available_driver] = False

        return booking_id, available_driver

    def cancel_cab(self, booking_id: str) -> bool:
        """
        Cancel a cab booking.
        Returns: True if cancellation successful, False otherwise
        """
        if booking_id not in self.bookings:
            return False

        booking = self.bookings[booking_id]
        if booking["status"] != "booked":
            return False

        # Free up driver
        driver_id = booking["driver_id"]
        self.driver_availability[driver_id] = True

        # Update booking status
        booking["status"] = "cancelled"
        booking["cancel_time"] = datetime.now()

        return True

    def get_driver_details(self, booking_id: str) -> Optional[dict]:
        """
        Get driver details for a booking.
        Returns: Driver details dictionary or None if booking not found/invalid
        """
        if booking_id not in self.bookings:
            return None

        booking = self.bookings[booking_id]
        if booking["status"] != "booked":
            return None

        driver_id = booking["driver_id"]
        return self.drivers.get(driver_id)


if __name__ == "__main__":
    service = CabBookingService()

    try:
        # Book a cab
        booking_id, driver_id = service.book_cab("123 Main St", "456 Oak Ave")
        print(f"Booking created: {booking_id} with driver {driver_id}")

        # Get driver details
        driver_details = service.get_driver_details(booking_id)
        print(f"Driver details: {driver_details}")

        # Cancel booking
        success = service.cancel_cab(booking_id)
        print(f"Cancellation successful: {success}")

        # Try to get driver details after cancellation
        driver_details = service.get_driver_details(booking_id)
        print(f"Driver details after cancellation: {driver_details}")

    except ValueError as e:
        print(f"Error: {e}")
