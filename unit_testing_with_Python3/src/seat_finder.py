class SeatFinder:
    def __init__(self, available_seats):
        """Initialize with a set of available seats."""
        self.available_seats = available_seats

    def find_seats(self, num_seats):
        """Find and return available seats based on the requested number of seats."""
        # Prefer seats in the front row if possible
        front_row_seats = {seat for seat in self.available_seats if seat[0] == 'A'}

        if num_seats == 1:
            # Return the front row seat, if available
            if front_row_seats:
                return {min(front_row_seats)}
            # Otherwise return any available seat
            return {min(self.available_seats)}

        # Check if there are enough seats available
        if len(self.available_seats) < num_seats:
            return {}  # Return empty if there are not enough seats

        # Try to find adjacent seats
        adjacent_seats = self._find_adjacent_seats(num_seats)
        if adjacent_seats:
            return adjacent_seats

        # If adjacent seats aren't available, return separate seats
        separate_seats = self._find_separate_seats(num_seats)
        return separate_seats

    def _find_adjacent_seats(self, num_seats):
        """Try to find adjacent seats."""
        seats = sorted(self.available_seats)
        for i in range(len(seats) - num_seats + 1):
            if all(ord(seats[i + j][1]) == ord(seats[i][1]) + j for j in range(num_seats)):
                return set(seats[i:i + num_seats])
        return None

    def _find_separate_seats(self, num_seats):
        """If adjacent seats aren't available, return separate seats."""
        # Simply select the first num_seats available seats, no proximity preference
        return {seat for seat in sorted(self.available_seats)[:num_seats]}
