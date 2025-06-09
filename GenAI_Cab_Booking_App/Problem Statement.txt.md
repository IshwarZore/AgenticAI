Implement MCP server for the following use case.

MakeYourTrip travel agency has developed a new Cab Service platform that integrates Google Maps technology with their proprietary cab booking system. This comprehensive solution enables customers to plan their travel itinerary through a streamlined process.

The new cab service platform offers several key features:

- Book a cab to your desired destination
- Cancel existing reservations when plans change
- Access detailed driver information

Through Claude desktop you can ask questions such as,

1. I want to travel from Vadodara to Ahmedabad and have around 8 hours in which I plan to visit 3 must visit places in ahmedabad. Plan the trip accordingly, such that I can visit all the places within the given time-range of 8hrs. Also book the cabs for this trip.
2. I'm visiting Delhi for a weekend. Create an itinerary for seeing major landmarks and arrange transportation between them.
3. Help me find the best street food locations in Lucknow and create an efficient route with cab bookings between stops.

This MCP server will use a prebuilt google maps MCP server to access maps api. And it will use your own MCP server for cab service that will have support for the following functions,

1. book_cab(pickup_location, dropoff_location)
2. cancel_cab(booking_id)
3. get_driver_details(booking_id)

Solution is given in the solution file. I know you are a sincere student, so however tempting it is, you will not click on the solution unless you have tried building it on your own 😄 Wish you all the best 👍🏼