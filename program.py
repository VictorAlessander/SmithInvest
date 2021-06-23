# coding: UTF-8

from core.status_invest import StatusInvest
import sys


def main(choice):
    if choice == 1:
        tickers = sys.argv[2::]

        status_invest = StatusInvest(tickers)
        status_invest.start()
        status_invest.finish()


if __name__ == "__main__":
    print(
        """

   SSSSSSSSSSSSSSS                         iiii         tttt        hhhhhhh                  IIIIIIIIII                                                                            tttt          
 SS:::::::::::::::S                       i::::i     ttt:::t        h:::::h                  I::::::::I                                                                         ttt:::t          
S:::::SSSSSS::::::S                        iiii      t:::::t        h:::::h                  I::::::::I                                                                         t:::::t          
S:::::S     SSSSSSS                                  t:::::t        h:::::h                  II::::::II                                                                         t:::::t          
S:::::S              mmmmmmm    mmmmmmm  iiiiiittttttt:::::ttttttt   h::::h hhhhh              I::::nnnn  nnnnnnnnvvvvvvv           vvvvvvveeeeeeeeeeee       ssssssssss  ttttttt:::::ttttttt    
S:::::S            mm:::::::m  m:::::::mmi:::::t:::::::::::::::::t   h::::hh:::::hhh           I::::n:::nn::::::::nv:::::v         v:::::ee::::::::::::ee   ss::::::::::s t:::::::::::::::::t    
 S::::SSSS        m::::::::::mm::::::::::mi::::t:::::::::::::::::t   h::::::::::::::hh         I::::n::::::::::::::nv:::::v       v:::::e::::::eeeee:::::ess:::::::::::::st:::::::::::::::::t    
  SS::::::SSSSS   m::::::::::::::::::::::mi::::tttttt:::::::tttttt   h:::::::hhh::::::h        I::::nn:::::::::::::::v:::::v     v:::::e::::::e     e:::::s::::::ssss:::::tttttt:::::::tttttt    
    SSS::::::::SS m:::::mmm::::::mmm:::::mi::::i     t:::::t         h::::::h   h::::::h       I::::I n:::::nnnn:::::nv:::::v   v:::::ve:::::::eeeee::::::es:::::s  ssssss      t:::::t          
       SSSSSS::::Sm::::m   m::::m   m::::mi::::i     t:::::t         h:::::h     h:::::h       I::::I n::::n    n::::n v:::::v v:::::v e:::::::::::::::::e   s::::::s           t:::::t          
            S:::::m::::m   m::::m   m::::mi::::i     t:::::t         h:::::h     h:::::h       I::::I n::::n    n::::n  v:::::v:::::v  e::::::eeeeeeeeeee       s::::::s        t:::::t          
            S:::::m::::m   m::::m   m::::mi::::i     t:::::t    ttttth:::::h     h:::::h       I::::I n::::n    n::::n   v:::::::::v   e:::::::e          ssssss   s:::::s      t:::::t    tttttt
SSSSSSS     S:::::m::::m   m::::m   m::::i::::::i    t::::::tttt:::::h:::::h     h:::::h     II::::::In::::n    n::::n    v:::::::v    e::::::::e         s:::::ssss::::::s     t::::::tttt:::::t
S::::::SSSSSS:::::m::::m   m::::m   m::::i::::::i    tt::::::::::::::h:::::h     h:::::h     I::::::::n::::n    n::::n     v:::::v      e::::::::eeeeeeee s::::::::::::::s      tt::::::::::::::t
S:::::::::::::::SSm::::m   m::::m   m::::i::::::i      tt:::::::::::th:::::h     h:::::h     I::::::::n::::n    n::::n      v:::v        ee:::::::::::::e  s:::::::::::ss         tt:::::::::::tt
 SSSSSSSSSSSSSSS  mmmmmm   mmmmmm   mmmmmiiiiiiii        ttttttttttt hhhhhhh     hhhhhhh     IIIIIIIIInnnnnn    nnnnnn       vvv           eeeeeeeeeeeeee   sssssssssss             ttttttttttt  
                                                                                            
    """
    )

    try:
        choice = int(sys.argv[1])
    except IndexError:
        print("Help: [1] Brasil / [2] America")

    main(choice)
