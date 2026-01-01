
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from fare_calculator import get_fare_and_validity
from station_data import get_distance

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_train_type(distance: int) -> str:
    """
    Determines the train type based on the distance.
    """
    if distance <= 100:
        return "Local / MEMU"
    else:
        return "Passenger"

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        'Welcome to the UTS Unreserved Ticket Assistant!\n\n'
        'Please tell me your journey details.\n'
        'For example: "Mumbai to Delhi"'
    )

# Define the message handler for journey details
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the user message with journey details."""
    user_input = update.message.text
    
    try:
        source, destination = user_input.lower().split(' to ')
        source_clean = source.strip()
        destination_clean = destination.strip()
        
        distance = get_distance(source_clean, destination_clean)
        
        if distance:
            fare, validity = get_fare_and_validity(distance)
            train_type = get_train_type(distance)
            
            rules = (
                "*Important Booking Rules:*\n"
                "• *Paperless Ticket:* Your phone is your ticket. Show the ticket in the UTS app when asked.\n"
                "• *Paper Ticket:* You must print the ticket from a kiosk at the station.\n"
                "• *GPS Requirement:* Your phone's GPS must be on and you must be within 2km of the source station to book a paperless ticket.\n"
                "• *Timings:* Avoid booking during peak hours (8-10am, 5-7pm) to avoid long queues at the station."
            )
            
            response = (
                f"Journey: {source.title()} to {destination.title()}\n"
                f"Train Type: {train_type} (estimated)\n"
                f"Fare: ₹{fare} (approx.)\n"
                f"Ticket Validity: {validity}\n\n"
                f"{rules}\n\n"
                "Book via UTS App: [Open UTS App](https://play.google.com/store/apps/details?id=com.cris.utsmobile)"
            )
            
            await update.message.reply_text(response, parse_mode='Markdown')
        else:
            await update.message.reply_text(
                "Sorry, I don't have the distance information for this route. "
                "I am actively working on expanding the station data."
            )

    except ValueError:
        await update.message.reply_text(
            'Please enter your journey details in the format "Source to Destination".'
        )

def main() -> None:
    """Start the bot."""
    # Get the token from environment variable
    token = os.getenv('TELEGRAM_TOKEN')
    if not token:
        logger.error("Telegram bot token not found in environment variables.")
        return

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - handle the message from user
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until the user presses Ctrl-C
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == '__main__':
    main()
