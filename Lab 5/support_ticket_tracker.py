"""Manage support tickets and their status."""

import json
import logging


TICKETS = {}


def create_ticket(
    # pylint: disable=too-many-arguments,too-many-positional-arguments
    title,
    description,
    reporter,
    priority="medium",
    category="general",
    audit_log=None,
):
    """Create and store a support ticket."""
    if not title:
        return None

    if audit_log is None:
        audit_log = []

    ticket_id = str(len(TICKETS) + 1)
    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": "open",
        "reporter": reporter,
        "assignee": None,
    }

    TICKETS[ticket_id] = ticket
    audit_log.append(f"Created ticket {ticket_id} for {reporter}")
    return ticket


def assign_ticket(ticket_id, agent):
    """Assign a ticket to an agent."""
    try:
        TICKETS[ticket_id]["assignee"] = agent
        return True
    except KeyError:
        return False


def update_status(ticket_id, status):
    """Update the status of a support ticket."""
    TICKETS[ticket_id]["status"] = status
    return TICKETS[ticket_id]


def search_tickets(status=None, priority=None):
    """Search tickets by status or priority."""
    r = []
    for t in TICKETS.values():
        if status is not None and t["status"] != status:
            continue
        if priority and t["priority"] != priority:
            continue
        r.append(t)
    return r


def save_tickets(path="tickets.json"):
    """Save all tickets to a JSON file."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(TICKETS, file)


def load_tickets(path="tickets.json"):
    """Load tickets from a JSON file."""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def print_ticket_report():
    """Print a summary of all support tickets."""
    print("Support Tickets")
    if not TICKETS:
        print("No tickets yet")
    for ticket_id, ticket in TICKETS.items():
        print(ticket_id, ticket["title"], ticket["status"])


def close_ticket(ticket_id):
    """Close a support ticket."""
    TICKETS[ticket_id]["status"] = "closed"


def is_open(ticket_id):
    """Check whether a ticket is open or in progress."""
    return TICKETS[ticket_id]["status"] in ("open", "in_progress")


def main():
    """Run the support ticket tracker."""
    logging.basicConfig(level=logging.INFO)
    create_ticket("Cannot sign in",
                  "Password reset link fails",
                  "alex@example.com")
    create_ticket("Billing question",
                  "Charged twice",
                  "lee@example.com",
                  "high")
    assign_ticket("1", "agent-01")
    update_status("1", "in_progress")
    print_ticket_report()
    logging.info("Tickets created: %s", len(TICKETS))
    print("Ticket 1 open?", is_open("1"))
    ticket_id = input("Ticket id to close (Enter to skip): ")
    if ticket_id:
        close_ticket(ticket_id)
    save_tickets()


if __name__ == "__main__":
    main()
