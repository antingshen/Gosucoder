#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

#define NUM_ITERS 15
#define DBL_MAX 500000000


float distance(float x1, float y1, float x2, float y2) {
  return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
}

int main(void) {
  srand48(0);
  int N, M;
  scanf("%d %d\n", &N, &M);
  float *points = malloc(2*(N+M)*sizeof(float));

  float *curr = points;
  float x, y;
  int i;
  for (i = 0; i < N; i++) {
    scanf("%f %f\n", &x, &y);
    *curr = x;
    curr++;
    *curr = y;
    curr++;
  }

  for (i = 0; i < M; i++) {
    float best_x, best_y;
    float best_dist = 0;
    float closest_dist, x, y;
    int iter;
    for (iter = 0; iter < NUM_ITERS; iter++) {
      x = drand48() * 1000.0;
      y = drand48() * 1000.0;
      closest_dist = DBL_MAX;
      
      for (curr = points; curr < points + (N + i)*2; curr+=2) {
        float d = distance(x, y, *curr, *(curr+1));
        assert(*curr >= 0 && *curr <= 1000);
        assert(d >= 0);
        if (d < closest_dist) {
          closest_dist = d;
        }
      }
      if (closest_dist > best_dist) {
        best_dist = closest_dist;
        best_x = x;
        best_y = y;
      }
    }
    *(points + (N + i)*2) = best_x;
    *(points + (N + i)*2 + 1) = best_y;
    printf("%f %f\n", best_x, best_y);
  }
  return 0;
}
