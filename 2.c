#include <stdlib.h>
#include <stdio.h>

#define DENSITY 10

struct Hint {
	int number;
	int truthy;
	char logic;
};

int isLie(int test, struct Hint hint) {
	switch (hint.logic) {
		case '<':
			return (test < hint.number) ^ hint.truthy;
		case '>':
			return (test > hint.number) ^ hint.truthy;
		case '=':
			return (test == hint.number) ^ hint.truthy;
	}
	exit(1);
}

int comp(const void *elem1, const void *elem2) {
	return *((int*) elem1) - *((int*) elem2);
}

int main(void) {
	int num_hints;
	scanf("%d\n", &num_hints);

	struct Hint *all_hints = malloc(num_hints*sizeof(struct Hint));
	struct Hint *hint_frontier = all_hints;
	int *candidates = malloc((num_hints+2)*sizeof(int));
	int *candidate_frontier = candidates;

	int i, j;
	char logic;
	int number;
	char *truthy_buffer = malloc(4);
	int truthy;
	for (i = 0; i < num_hints; i++) {
		scanf("%c %d %s\n", &logic, &number, truthy_buffer);
		truthy = *truthy_buffer == 'y' ? 1 : 0;
		struct Hint hint = {number, truthy, logic};
		*hint_frontier = hint;
		*candidate_frontier = number;
		hint_frontier++;
		candidate_frontier++;
	}

	qsort(candidates, sizeof(int), num_hints, comp);
	*candidate_frontier = 1<<30;
	*(candidate_frontier+1) = (1<<30) + 1;

	int minimum = 1<<30;
	int n = 1;
	for (i = 0; i < (num_hints+2); i++) {
		int new_n = *(candidates+ i);
		if (new_n == n) {
			continue;
		}
		int max_run = 0;
		int cur_run = 0;
		for (j = 0; j < num_hints; j++) {
			if (isLie(n, *(all_hints+j))) {
				cur_run++;
			} else {
				max_run = cur_run > max_run ? cur_run : max_run;
				cur_run = 0;
			}
		}
		max_run = cur_run > max_run ? cur_run : max_run;
		n = new_n;
		minimum = minimum < max_run ? minimum : max_run;
	}

	printf("%d\n", minimum);

	return 0;
}
