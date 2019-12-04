import pydux


def keep_card_reducer(state, action):
    if state is None:
        state = 0
    if action is None:
        return state
    elif action['type'] == 'INCREMENT':
        return state + 1
    elif action['type'] == 'DECREMENT':
        return state - 1
    return state


# Create a Redux store holding the state of your app.
# Its API is { subscribe, dispatch, get_state }.
keep_card_store = pydux.create_store(keep_card_reducer)

# You can use subscribe() to update the UI in response to state changes.
keep_card_store.subscribe(lambda: print(keep_card_store.get_state()))

# The only way to mutate the internal state is to dispatch an action.
# The actions can be serialized, logged or stored and later replayed.
keep_card_store.dispatch({'type': 'INCREMENT'})
# 1
keep_card_store.dispatch({'type': 'INCREMENT'})
# 2
keep_card_store.dispatch({'type': 'DECREMENT'})
# 1
