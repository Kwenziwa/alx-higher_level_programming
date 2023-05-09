#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @num: integer
 * @nxt: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int num;
	struct listint_s *nxt;
} listint_t;

listint_t *add_nodeint(listint_t **hd, const int num);
int check_cycle(listint_t *lst);
void free_listint(listint_t *hd);
size_t print_listint(const listint_t *hh);

#endif /* LISTS_H */
