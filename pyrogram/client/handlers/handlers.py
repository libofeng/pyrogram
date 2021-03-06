# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from .handler import Handler


class MessageHandler(Handler):
    """The Message handler class. Used to handle text, media and service messages coming from
    any chat (private, group, channel). It is intended to be used with
    :meth:`add_handler() <pyrogram.Client.add_handler>`

    Args:
        callback (``callable``):
            Pass a function that will be called when a new Message arrives. It takes *(client, message)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters <pyrogram.Filters>`):
            Pass one or more filters to allow only a subset of messages to be passed
            in your callback function.

    Other parameters:
        client (:obj:`Client <pyrogram.Client>`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        message (:obj:`Message <pyrogram.Message>`):
            The received message.
    """

    def __init__(self, callback: callable, filters=None):
        super().__init__(callback, filters)

    def check(self, message):
        return (
            self.filters(message)
            if self.filters
            else True
        )


class CallbackQueryHandler(Handler):
    """The CallbackQuery handler class. Used to handle callback queries coming from inline buttons.
    It is intended to be used with :meth:`add_handler() <pyrogram.Client.add_handler>`

    Args:
        callback (``callable``):
            Pass a function that will be called when a new CallbackQuery arrives. It takes *(client, callback_query)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`Filters <pyrogram.Filters>`):
            Pass one or more filters to allow only a subset of callback queries to be passed
            in your callback function.

    Other parameters:
        client (:obj:`Client <pyrogram.Client>`):
            The Client itself, useful when you want to call other API methods inside the message handler.

        callback_query (:obj:`CallbackQuery <pyrogram.CallbackQuery>`):
            The received callback query.
    """

    def __init__(self, callback: callable, filters=None):
        super().__init__(callback, filters)

    def check(self, callback_query):
        return (
            self.filters(callback_query)
            if self.filters
            else True
        )


class RawUpdateHandler(Handler):
    """The Raw Update handler class. Used to handle raw updates. It is intended to be used with
    :meth:`add_handler() <pyrogram.Client.add_handler>`

    Args:
        callback (``callable``):
            A function that will be called when a new update is received from the server. It takes
            *(client, update, users, chats)* as positional arguments (look at the section below for
            a detailed description).

    Other Parameters:
        client (:class:`Client <pyrogram.Client>`):
            The Client itself, useful when you want to call other API methods inside the update handler.

        update (``Update``):
            The received update, which can be one of the many single Updates listed in the *updates*
            field you see in the :obj:`Update <pyrogram.api.types.Update>` type.

        users (``dict``):
            Dictionary of all :obj:`User <pyrogram.api.types.User>` mentioned in the update.
            You can access extra info about the user (such as *first_name*, *last_name*, etc...) by using
            the IDs you find in the *update* argument (e.g.: *users[1768841572]*).

        chats (``dict``):
            Dictionary of all :obj:`Chat <pyrogram.api.types.Chat>` and
            :obj:`Channel <pyrogram.api.types.Channel>` mentioned in the update.
            You can access extra info about the chat (such as *title*, *participants_count*, etc...)
            by using the IDs you find in the *update* argument (e.g.: *chats[1701277281]*).

    Note:
        The following Empty or Forbidden types may exist inside the *users* and *chats* dictionaries.
        They mean you have been blocked by the user or banned from the group/channel.

        - :obj:`UserEmpty <pyrogram.api.types.UserEmpty>`
        - :obj:`ChatEmpty <pyrogram.api.types.ChatEmpty>`
        - :obj:`ChatForbidden <pyrogram.api.types.ChatForbidden>`
        - :obj:`ChannelForbidden <pyrogram.api.types.ChannelForbidden>`
    """

    def __init__(self, callback: callable):
        super().__init__(callback)
