def merge_sorted(head1, head2):
  
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  merged_head = None 
  if head1.data <= head2.data:
    merged_head = head1
    head1 = head1.next
  else:
    merged_head = head2
    head2 = head2.next

  merged_tail = merged_head
  while head1 != None and head2 != None:
    new_head = None 
    if head1.data <= head2.data:
      new_head = head1
      head1 = head1.next
    else:
      new_head = head2
      head2 = head2.next
    
    merged_tail.next = new_head
    merged_tail = new_head

  if head1 != None:
    merged_tail.next = head1
  elif head2 != None:
    merged_tail.next = head2

  return merged_head


if __name__ == "__main__":
    array1 = [2, 3, 5, 6]
    array2 = [1, 4, 10]