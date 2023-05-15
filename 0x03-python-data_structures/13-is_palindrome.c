#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @hd: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **hd)
{
  listint_t *previous = NULL;
  listint_t *current = *hd;
  listint_t *next = NULL;

  while (current)
    {
      next = current->next;
      current->next = previous;
      previous = current;
      current = next;
    }

  *hd = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @hd: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **hd)
{
  listint_t *aslow = *hd, *fast = *hd, *tmp = *hd, *dup = NULL;

  if (*hd == NULL || (*hd)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = aslow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = aslow->next->next;
	  break;
	}
      aslow = aslow->next;
    }

  reverse_listint(&dup);

  while (dup && tmp)
    {
      if (tmp->n == dup->n)
	{
	  dup = dup->next;
	  tmp = tmp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}
