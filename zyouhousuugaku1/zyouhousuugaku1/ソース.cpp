/*/
 * C����̃T���v���v���O���� - Webkaru
 * - �t�B�{�i�b�`���̌v�Z -
 */
#include <stdio.h>

int main(void) {
    /* �ϐ��̐錾 */
    int n;
    int f0, f1, f2;

    f0 = 0;
    f1 = 1;

    /* �t�B�{�i�b�`��(n=0)�̏o�� */
    printf("%d\n", f0);

    /* �t�B�{�i�b�`���̌v�Z */
    while (f1 < 100000000) {
        // �t�B�{�i�b�`���̏o��(n>0)
        printf("%d\n", f1);
        // �t�B�{�i�b�`���̌v�Z
        f2 = f1 + f0;
        // �ϐ��̑��
        f0 = f1;
        f1 = f2;
    }

    return 0;
}