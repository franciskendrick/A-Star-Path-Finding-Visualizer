from .clip import clip


def separate_sets_from_xaxis(spriteset, separator_color, y=0):
    separated_sets = []
    current_wd = 0

    # Loop over every pixel in the given Y coordinate in the given spriteset
    for x in range(spriteset.get_width()):
        pixel = spriteset.get_at((x, y))

        # A sprite has been found
        if pixel == separator_color:
            # Clip spriteset
            set = clip(
                spriteset,
                (x - current_wd, 0),
                (current_wd, spriteset.get_height())
            )

            # Append clipped spriteset to separated sets
            separated_sets.append(set)

            # Update current width
            current_wd = 0
        else:
            # Update current width
            current_wd += 1

    # Return
    return separated_sets


def separate_sets_from_yaxis(spriteset, separator_color, x=0):
    separated_sets = []
    current_ht = 0

    # Loop over every pixel in the given X coordinate in the given spriteset
    for y in range(spriteset.get_height()):
        pixel = spriteset.get_at((x, y))

        # A sprite has been found
        if pixel == separator_color:
            # Clip spriteset
            set = clip(
                spriteset,
                (0, y - current_ht),
                (spriteset.get_width(), current_ht)
            )

            # Append clipped spriteset to separated sets
            separated_sets.append(set)

            # Update current height
            current_ht = 0
        else:
            # Update current height
            current_ht += 1

    # Return
    return separated_sets
