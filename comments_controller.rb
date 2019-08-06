class CommentsController < ApplicationController
  def create
     @Articale = Articale.find(params[:articale_id])
     @comment = @Articale.comments.create(params[:comment].permit(:lok,:comment))
     redirect_to articale_path(@Articale)
  end
  def destroy
    @Articale = Articale.find(params[:articale_id])
    @comment = @Articale.comments.find(params[:id])
    @comment.destroy
    redirect_to articale_path(@Articale)

  end

  #def comment_params
  #  params.require(:comment).permit(:lok)

  #end

end
