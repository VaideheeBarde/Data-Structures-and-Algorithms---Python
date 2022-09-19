def generate_balanced_parantheses(num_pairs):
    def directed_generate_balanced_parantheses(num_left_parens_needed, num_right_parens_needed, valid_prefix, result=[]):

        if num_left_parens_needed > 0:
            directed_generate_balanced_parantheses(num_left_parens_needed - 1, num_right_parens_needed, valid_prefix + '(')

        if num_left_parens_needed < num_right_parens_needed:
            directed_generate_balanced_parantheses(num_left_parens_needed, num_right_parens_needed - 1, valid_prefix + ')')

        if not num_right_parens_needed:
            result.append(valid_prefix)

        return result

    return directed_generate_balanced_parantheses(num_pairs, num_pairs, '')

print(generate_balanced_parantheses(2))