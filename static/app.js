pickStoryForm = document.getElementById("pick-story-form");
storySelect = document.getElementById("story-select");

pickStoryForm.addEventListener("submit", handleFormSubmit);

	function handleFormSubmit(){
		storyName = storySelect.value;
		pickStoryForm.action = "/" + storyName;
	}