from mcp.server.fastmcp import FastMCP

from booking import CabBookingService

mcp = FastMCP("cab-service")
cab_service = CabBookingService()


@mcp.tool()
def book_cab(pickup_location, dropoff_location):
    """
    Book a cab from pickup_location to dropoff_location.
    Args:
        pickup_location (str): The location where the cab should pick you up.
        dropoff_location (str): The location where you want to go.
    
    Returns:
        dict: A dictionary containing booking details.
    """
    booking_id, driver_id = cab_service.book_cab(pickup_location, dropoff_location)
    print(f"Booking created: {booking_id} with driver {driver_id}")
    return {"booking_id": booking_id,
            "booking_details": cab_service.bookings[booking_id]}


@mcp.tool()
def cancel_cab(booking_id):
    """
    Cancel a cab booking with the given booking_id.
    Args:
        booking_id (str): The ID of the booking to cancel.
    Returns:
        bool: True if cancellation was successful, False otherwise.
    """
    success = cab_service.cancel_cab(booking_id)
    if success:
        print(f"Booking {booking_id} cancelled successfully.")
    else:
        print(f"Failed to cancel booking {booking_id}.")
    return success


@mcp.tool()
def get_driver_details(booking_id):
    """
    Get driver details for the given booking_id.
    Args:
        booking_id (str): The ID of the booking.
    Returns:
        dict: A dictionary containing driver details or None if not found.
    """
    driver_details = cab_service.get_driver_details(booking_id)
    if driver_details:
        print(f"Driver details for booking {booking_id}: {driver_details}")
    else:
        print(f"No driver details found for booking {booking_id}.")
    return driver_details


if __name__ == "__main__":
    mcp.run(transport="stdio")
