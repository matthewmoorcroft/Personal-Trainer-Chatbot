
def analyse_volume_performance(user_name, user_gender, weight_rate, bfr_rate):
    """ Conditions for volume improvement
        Weight ⬆
        Body fat ratio ⬇
    """
    new_routine = False

    if weight_rate > 0 and bfr_rate < 0:
        msg = f"""{user_name} after analysing your data I have seen
                you are gaining volume and improving your body to fat ratio, keep the nice work going"""
    else:
        msg = f"""{user_name} after reviewing your data I think we should consider changing strategy,
                we are not reaching out objectives, let's try a different strategy and see if this works best."""
        new_routine = True

    return msg, new_routine


def analyse_weight_loss_performance(user_name, user_gender, weight_rate, bfr_rate):
    """ Conditions for weight loss improvement
        Weight ⬇
        Body fat ratio ⬇
    """
    if weight_rate < 0 and bfr_rate < 0:
        msg = f"""{user_name} after analysing your data I am very happy to see
                you are loosing weight and improving your body to fat ratio, keep the nice work going"""
    else:
        msg = f"""{user_name} after reviewing your data I think we should consider changing strategy,
                we are not reaching out objectives, let's try a different strategy and see if this works best."""
        new_routine = True

    return msg, new_routine


def analyse_definition_performance(user_name, user_gender, weight_rate, bfr_rate):
    """ Conditions for definition improvement
        Weight ⬆⬇
        Body fat ratio ⬇
    """
    if bfr_rate < 0 and weight_rate > (-2):
        msg = f"""{user_name} after analysing your data I have seen you are improving your body to fat
                ratio balancing it well with your weight, keep the nice work going"""
    else:
        msg = f"""{user_name} after reviewing your data I think we should consider changing strategy,
                we are not reaching out objectives, let's try a different strategy and see if this works best."""
        new_routine = True

    return msg, new_routine


def verify_enough_data_to_analyse(data):
    value_i = None
    pos_i = None

    for pos, item in enumerate(data):
        if item is not None:
            value_i = item
            pos_i = pos
            break

    data.reverse()
    value_f = None
    pos_f = None

    for pos, item in enumerate(data):
        if item is not None:
            value_f = item
            pos_f = pos
            break

    pos_f = 12 - pos_f

    res = pos_f - pos_i

    if res > 3:
        return True, value_i, value_f
    else:
        return False, None, None


def get_progress_info(user_id, telegram_id, user_name, training_type, user_gender, weights, bodyfatratios):

    weight = [None, None, None, None, None, None, None, None, None, None, None, None]

    # bfr = [23, 22, 21, 20, 19, 19, 18, 18, 17, 16, 15, 14]
    bfr = [None, None, None, None, None, None, None, None, None, None, None, None]

    for key, item in weights.items():
        weight[int(key)-1] = float(item)

    for key, item in bodyfatratios.items():
        bfr[int(key)-1] = float(item)

    do_analyse_weights, weight_i, weight_f = verify_enough_data_to_analyse(weight)
    do_analyse_bfr, bfr_i, bfr_f = verify_enough_data_to_analyse(bfr)

    weight_rate = (weight_f/weight_i - 1) * 100
    bfr_rate = (bfr_f/bfr_i - 1) * 100

    if do_analyse_bfr and do_analyse_weights:
        if training_type == "volume":
            perf_msg, new_routine = analyse_volume_performance(
                user_name, user_gender, weight_rate, bfr_rate)
        elif training_type == "weight_loss":
            perf_msg, new_routine = analyse_weight_loss_performance(
                user_name, user_gender, weight_rate, bfr_rate)
        else:
            perf_msg, new_routine = analyse_definition_performance(
                user_name, user_gender, weight_rate, bfr_rate)

        return perf_msg, new_routine

    perf_msg = f"""{user_name} I don't have enough information to get a
                conclusion on your results, here is a graph so you can
                check how you are doing."""

    return perf_msg, False
